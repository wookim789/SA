from django.db import models

# Create your models here.


class UserCount(models.Model):
    userId = models.CharField(max_length=10)
    userPw = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    teamCount = models.IntegerField(default=0)


class TeamInfo(models.Model):
    teamName = models.CharField(max_length=10, null=True)
    userId = models.CharField(max_length=10)
    leader = models.IntegerField(default=0)


class TemaPlanList(models.Model):
    teamPlanNo = models.IntegerField(primary_key=True)
    teamPlanName = models.CharField(max_length=10)
    teamName = models.CharField(max_length=10, null=True)


class SelectDate(models.Model):
    teamName = models.CharField(max_length=10, null=True)
    teamPlanNo = models.IntegerField(default=0)
    userId = models.CharField(max_length=10)
    selectDate = models.CharField(max_length=10)
    dateCount = models.IntegerField(default=0)
    confirmIndicator = models.IntegerField(default=0)


class PlanMap(models.Model):
    teamName = models.CharField(max_length=10, null=True)
    teamPlanNo = models.IntegerField(default=0)
    selectDate = models.CharField(max_length=10)
    userId = models.CharField(max_length=10)
    pickCount = models.IntegerField()
    userColor = models.CharField(max_length=10)
    lat = models.IntegerField(default=0)
    lng = models.IntegerField(default=0)
    address = models.CharField(max_length=10)
    confirm = models.IntegerField(default=0)
