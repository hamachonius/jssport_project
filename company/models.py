from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    summary_or_promotion = models.TextField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    evaluation = models.IntegerField(default=1)
    companyid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
