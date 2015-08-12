from django.contrib.gis.db import models
from geopy.geocoders import Nominatim

# Create your models here.
class MyModel(models.Model):
    location = models.PointField()
    description = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=False)
    
    @property
    def address (self):
        geolocator = Nominatim()
        address = geolocator.reverse("%lf, %lf" % (self.location.y, self.location.x))
        if (address != None):
            return ((address))
        else:
            return ("")
