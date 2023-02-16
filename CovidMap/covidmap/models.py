from django.db import models
# Create your models here.

class Province(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class pandemic(models.Model):
    province = models.ForeignKey(Province,on_delete=models.CASCADE)
    infected = models.CharField(max_length=100)
    death = models.CharField(max_length=100)
    recovered =  models.CharField(max_length=100)
