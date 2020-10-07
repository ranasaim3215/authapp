from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    officeName = models.CharField(max_length=200)
    age = models.IntegerField()
    date = models.DateField()
    salary = models.IntegerField()
    image = models.ImageField(upload_to='upload/')
    def __str__(self):
        return self.name