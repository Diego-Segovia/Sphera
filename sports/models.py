from django.db import models

# Create your models here.

class Host(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    country = models.CharField(max_length=20)

class Match(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    location = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    host = models.ForeignKey('Host', on_delete=models.CASCADE, null=True)