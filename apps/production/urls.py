from django.urls import path
from production import views

urlpatterns = [
    path("seed/", views.SeedAPIView.as_view(), name="seed"),
    path("terrain/", views.TerrainAPIView.as_view(), name="terrain"),
    path("lot/", views.LotAPIView.as_view(), name="lot"),
    path("crop/", views.CropAPIView.as_view(), name="crop"),
    path("harvest/", views.HarvestAPIView.as_view(), name="harvest"),
]
