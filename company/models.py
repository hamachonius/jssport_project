from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    introduction = models.TextField()
    url = models.URLField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    evaluation = models.IntegerField(default=1)
    regi_date = models.DateTimeField()
    companyid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.regi_date.strftime('%b %e %Y')
