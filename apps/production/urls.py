from django.urls import path
from production import views

urlpatterns = [
    path("seed/", views.SeedAPIView, name="seed"),
    path("terrain/", views.TerrainAPIView, name="terrain"),
    path("lot/", views.LotAPIView, name="lot"),
    path("crop/", views.CropAPIView, name="crop"),
    path("harvest/", views.HarvestAPIView, name="harvest"),
]
