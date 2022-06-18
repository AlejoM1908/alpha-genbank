from django.db import models
from helpers.models import TrackingModel

class SeedModel(TrackingModel):
    readonly_fields = ("id",)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    genetic_purity = models.SmallIntegerField()

class TerrainModel(TrackingModel):
    readonly_fields = ("id",)
    area = models.FloatField()
    tag = models.CharField(max_length=50)
    type = models.CharField(max_length=20)  

class LotModel(TrackingModel):
    readonly_fields = ("id",)
    tr_id = models.ForeignKey(TerrainModel, on_delete=models.CASCADE)
    target_purity = models.SmallIntegerField()
class CropModel(TrackingModel):
    readonly_fields = ("id",)
    lt_id = models.ForeignKey(LotModel, on_delete= models.CASCADE)
    se_id = models.ForeignKey(SeedModel, on_delete= models.CASCADE)
    type = models.CharField(max_length= 50)
    projected_date= models.DateField()

class HarvestModel(TrackingModel):
    readonly_fields = ("id",)
    lt_id = models.ForeignKey(LotModel, on_delete=models.CASCADE)
    flower = models.FloatField()
    waste = models.FloatField()
