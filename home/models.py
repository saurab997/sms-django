from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    Class = models.CharField()
    roll = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.Class
    