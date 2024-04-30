from django.db import models

# Create your models here.

class nature(models.Model):
    seasons=models.CharField(max_length=100)
    weather=models.ImageField()
    fruit=models.ImageField()
    tempature=models.IntegerField()
    habitat=models.ImageField()

class flora(models.Model):
    name=models.CharField(max_length=50)
    pictures=models.ImageField()
                           
    def _str_(self):
        return self.name

class fauna(models.Model):
    name=models.CharField(max_length=50)
    livingstyle=models.ImageField()

    def _str_(self):
        return self.name




 