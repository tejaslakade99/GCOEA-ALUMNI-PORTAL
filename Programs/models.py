from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contests(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    contest_name = models.CharField(max_length=200)
    platform_title = models.CharField(max_length=200)
    platform_link = models.URLField(max_length=500)
    coordinator = models.CharField(max_length=200)
    contest_date = models.DateTimeField()
    contact_to = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)


class Events(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    event_name = models.CharField(max_length=200)
    platform_title = models.CharField(max_length=200)
    platform_link = models.URLField(max_length=500)
    speaker = models.CharField(max_length=200)
    event_date = models.DateTimeField()
    contact_to = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
