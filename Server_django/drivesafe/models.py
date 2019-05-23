from django.db import models

# Create your models here.

class gps_coordinates(models.Model):
    time = models.DateTimeField()
    lat = models.CharField(max_length= 50)
    lon = models.CharField(max_length= 50)
    def __str__(self):
        return str(self.lat+"~"+self.lon)