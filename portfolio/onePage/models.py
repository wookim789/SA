from django.db import models

# Create your models here.
class selectDate(models.Model):
    userId = models.CharField(max_length=10)
    selectedDate = models.CharField(max_length=10)
    likeNum = models.IntegerField(max_length=3)
    saveDate = models.BooleanField()