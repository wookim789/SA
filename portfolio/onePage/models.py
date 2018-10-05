from django.db import models

# Create your models here.


class SelectDate(models.Model):
    userId = models.CharField(max_length=10)
    selectDate = models.CharField(max_length=10)
    dateCount = models.IntegerField(default=0)
    confirmIndicator = models.IntegerField(default=0)
