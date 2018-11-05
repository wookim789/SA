from django.db import models

# Create your models here.


class UserCount(models.Model):
    userId = models.CharField(max_length=10)
    userPw = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    teamCount = models.IntegerField()


class TeamInfo(models.Model):
    teamName = models.CharField(max_length=10)
    userId = models.CharField(max_length=10)
    leader = models.IntegerField()


class TemaPlanList(models.Model):
    teamName = models.CharField(max_length=10)
    teamPlanNo = models.IntegerField()
    teamPlanName = models.CharField(max_length=10)


class SelectDate(models.Model):
    teamPlanNo = models.IntegerField()
    userId = models.CharField(max_length=10)
    selectDate = models.CharField(max_length=10)
    dateCount = models.IntegerField(default=0)
    confirmIndicator = models.IntegerField(default=0)


class PlanMap(models.Model):
    teamPlanNo = models.IntegerField()
    selectDate = models.CharField(max_length=10)
    userId = models.CharField(max_length=10)
    pickCount = models.IntegerField()
    userColor = models.CharField(max_length=10)
    lat = models.IntegerField()
    lng = models.IntegerField()
    address = models.CharField(max_length=10)
    confirm = models.IntegerField()
