from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from production.models import SeedModel, LotModel, CropModel, HarvestModel, TerrainModel
# Register your models here.
admin.site.register(SeedModel)
admin.site.register(LotModel)
admin.site.register(CropModel)
admin.site.register(HarvestModel)
admin.site.register(TerrainModel)
