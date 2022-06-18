from dataclasses import fields
from rest_framework import serializers
from production.models import SeedModel, TerrainModel, LotModel, CropModel, HarvestModel

class SeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeedModel
        fields = (
            "id",
            "type",
            "name",
            "genetic_purity",
        )

class TerrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerrainModel
        fields = (
            "id",
            "type",
            "area",
            "tag",
        )

class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotModel
        fields = (
            "id",
            "tr_id",
            "target_purity",
        )

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropModel
        fields = (
            "id",
            "type",
            "lt_id",
            "se_id",
            "projected_date"
        )

class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestModel
        fields = (
            "id",
            "lt_id",
            "flower",
            "waste",
        )
