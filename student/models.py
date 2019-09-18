from django.db import models


# Create your models here.
class stud(models.Model):
    naam = models.CharField(max_length=100, null=False, blank=False)
    roll = models.IntegerField(unique=True)
    Branch = models.CharField(max_length=50, null=False, blank=False)
    sem = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.roll)


class society(models.Model):
    Ganesh_puja = models.CharField(max_length=100, null=False, blank=False)
    Teachers_day = models.CharField(max_length=100, null=False, blank=False)
    Orientation = models.CharField(max_length=100, null=False, blank=False)
    Saraswati_puja = models.CharField(max_length=100, null=False, blank=False)
    Freshers = models.CharField(max_length=100, null=False, blank=False)
    Picnic = models.CharField(max_length=100, null=False, blank=False)
    Farewell = models.CharField(max_length=100, null=False, blank=False)
