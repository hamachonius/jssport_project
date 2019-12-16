from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Jishusei(models.Model):
    name = models.CharField(max_length=50)
    introduction = models.TextField()
    edu_background_duration_y = models.IntegerField()
    edu_background_duration_m = models.IntegerFields()

    carrer_background = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pic/')
