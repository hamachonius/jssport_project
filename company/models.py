from django.db import models

# Create your models here.
class Company(models.Model):
    title = models.CharField(max_length=100)
    companyname = models.CharField(max_length=20)
    url = models.URLField()
    image = ImageField()
    evaluation = models.IntegerField(default=1)
