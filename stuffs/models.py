from django.db import models
from django.db.models.aggregates import Count
from django.db.models.base import Model

# Create your models here.
class gpu(models.Model):
    graphics_card_ram_size = models.SmallIntegerField()
    series=models.CharField(max_length=10)
    computer_memory_type = models.CharField(max_length=10)
    new_or_stock = models.NullBooleanField()
    issue = models.CharField(max_length=100)
    countX=models.SmallIntegerField()
    etc = models.CharField(max_length=100)

    def __str__(self):
        return self.description