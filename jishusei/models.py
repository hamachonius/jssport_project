from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Jishusei(models.Model):
    name = models.CharField(max_length=50)
    introduction = models.TextField()
    edu_background = models.TextField()
    carrer_background = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pic/')
