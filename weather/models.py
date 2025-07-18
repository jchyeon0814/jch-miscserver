from django.db import models

class AdminRegion(models.Model):
    region_code = models.CharField(max_length=10, primary_key=True)
    level_1 = models.CharField(max_length=50)
    level_2 = models.CharField(max_length=50, null=True)
    level_3 = models.CharField(max_length=50, null=True)
    grid_x = models.IntegerField()
    grid_y = models.IntegerField()
    longitude_deg = models.IntegerField()
    longitude_min = models.IntegerField()
    longitude_sec = models.FloatField()
    latitude_deg = models.IntegerField()
    latitude_min = models.IntegerField()
    latitude_sec = models.FloatField()
    longitude_sec_100 = models.FloatField()
    latitude_sec_100 = models.FloatField()
    location_updated = models.DateTimeField()
    
    class Meta:
        db_table = 'admin_region'