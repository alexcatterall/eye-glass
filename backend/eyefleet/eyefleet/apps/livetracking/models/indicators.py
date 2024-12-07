from django.db import models
from telemex.utils.logger import logger

# DEFINE OPTION MODELS
class DataType(models.Model):
    id = models.CharField(max_length=50, primary_key=True)

    class Meta:
        db_table = 'data_types'


    def __str__(self):
        return self.id
    
    @classmethod
    def get_defaults(cls):
        defaults = [ 'integer', 'float', 'boolean', 'string' ]
        return [cls(id=id) for id in defaults]

# DEFINE CORE MODELS
class Indicator(models.Model):
    id = models.CharField(max_length=20, 
                          primary_key=True,
                          unique=True, 
                          default='IND-')
    name = models.CharField(max_length=255, unique=True)
    computed = models.BooleanField(default=False)
    compute_func = models.CharField(max_length=255, null=True, 
                                   blank=True,
                                   help_text="Function to compute indicator")
    data_type = models.ForeignKey(DataType, on_delete=models.PROTECT, null=True, blank=True)
    unit = models.CharField(max_length=50, default="unk",
                            help_text="unit of measurement")
    CAN_bus_code = models.CharField(max_length=50, null=True, blank=True,
                                   help_text="CAN bus code to read indicator")
    description = models.TextField(null=True, blank=True)

    min_value = models.FloatField(null=True, blank=True)
    max_value = models.FloatField(null=True, blank=True)

    warning_threshold = models.FloatField(null=True, blank=True)
    critical_threshold = models.FloatField(null=True, blank=True)

    enabled = models.BooleanField(default=True)
    last_reading = models.FloatField(null=True, blank=True)
    last_reading_time = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'indicators'

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        if not self.id or self.id == 'IND-':
            last = Indicator.objects.last()
            if last:
                num = int(last.id.split('-')[1]) + 1
                self.id = f'IND-{num:08d}'
            else:
                self.id = f'IND-00000001'
        super().save(*args, **kwargs)

    def compute_value(self, value):
        if self.computed:
            try:
                if self.data_type.id == 'integer':
                    value = int(value)
                    return int(eval(self.compute_func))
                elif self.data_type.id == 'float':
                    value = float(value)
                    return float(eval(self.compute_func))
                elif self.data_type.id == 'boolean':
                    value = bool(value)
                    return bool(eval(self.compute_func))
                elif self.data_type.id == 'string':
                    value = str(value)
                    return str(eval(self.compute_func))
                else:
                    return eval(self.compute_func)
            except Exception as e:
                logger.error(f"Error computing indicator {self.id}: {e}")
        return value

    def validate_value(self, value):
        if self.min_value and value < self.min_value:
            return False
        if self.max_value and value > self.max_value:
            return False
        return True