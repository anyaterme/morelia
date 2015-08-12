# Register your models here.
from django.contrib.gis import admin
from models import MyModel
from pyproj import Proj, transform
from geopy.geocoders import Nominatim


class MyModelAdmin(admin.OSMGeoAdmin):
    default_lon, default_lat = transform(Proj(init='epsg:4326'), Proj(init='epsg:3857'), -101.193445, 19.702716) 
    default_zoom = 15
    list_display = ('description', 'date', 'address')
    ordering = ["-date"]
    
admin.site.register(MyModel, MyModelAdmin)

