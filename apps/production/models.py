from django.db import models
from helpers.models import TrackingModel
from django.utils.translation import gettext_lazy as _

class SeedModel(TrackingModel):
    readonly_fields = ("id",)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    genetic_purity = models.SmallIntegerField()

    def create_seed(self, type, name, genetic_purity, **extra_fields):
        if not type:
            raise ValueError("The given type must be set")
        if not name:
            raise ValueError("The given name must be set")
        if not genetic_purity:
            raise ValueError("The given genetic purity must be set")
        
        seed = self.model(type=type, name=name, genetic_purity=genetic_purity, **extra_fields)
        seed.save(using=self._db)
        return seed

class TerrainModel(TrackingModel):
    readonly_fields = ("id",)
    area = models.FloatField()
    tag = models.CharField(max_length=50)
    type = models.CharField(max_length=20)

    def create_terrain(self, area, tag, type, **extra_fields):
        if not area:
            raise ValueError("The given area must be set")
        if not tag:
            raise ValueError("The given tag must be set")
            
        terrain = self.model(area=area, tag=tag, type=type, **extra_fields)
        terrain.save(using=self._db)
        return terrain
    

class LotModel(TrackingModel):
    readonly_fields = ("id",)
    tr_id = models.ForeignKey(TerrainModel, on_delete=models.CASCADE)
    target_purity = models.SmallIntegerField()

    def create_lot(self, tr_id, target_purity, **extra_fields):
        if not tr_id:
            raise ValueError("The given tr_id must be set")
        if not target_purity:
            raise ValueError("The given target_purity must be set")
        
        lot = self.model(tr_id=tr_id, target_purity=target_purity, **extra_fields)
        lot.save(using=self._db)
        return lot

class CropModel(TrackingModel):
    readonly_fields = ("id",)
    lt_id = models.ForeignKey(LotModel, on_delete= models.CASCADE)
    se_id = models.ForeignKey(SeedModel, on_delete= models.CASCADE)
    type = models.CharField(max_length= 50)
    projected_date= models.DateField()

    def create_crop(self, lt_id, se_id, type, projected_date, **extra_fields):
        if not lt_id:
            raise ValueError("The given lt_id must be set")
        if not se_id:
            raise ValueError("The given se_id must be set")
        if not type:
            raise ValueError("The given type must be set")
        
        crop = self.model(lt_id=lt_id, se_id=se_id, type=type, projected_date=projected_date, **extra_fields)
        crop.save(using=self._db)
        return crop
    
class HarvestModel(TrackingModel):
    readonly_fields = ("id",)
    lt_id = models.ForeignKey(LotModel, on_delete=models.CASCADE)
    flower = models.FloatField()
    waste = models.FloatField()
    
    def create_harvest(self, lt_id, flower, waste, **extra_fields):
        if not lt_id:
            raise ValueError("The given lt_id must be set")
        if not flower:
            raise ValueError("The given flower must be set")
        if not waste:
            raise ValueError("The given waste must be set")
        
        harvest = self.model(lt_id=lt_id, flower=flower, waste=waste, **extra_fields)
        harvest.save(using=self._db)
        return harvest
