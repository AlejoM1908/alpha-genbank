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

    def create(self, validated_data):
        return SeedModel.objects.create_seed(**validated_data)



class TerrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerrainModel
        fields = (
            "id",
            "type",
            "area",
            "tag",
        )

    def create(self, validated_data):
        return TerrainModel.objects.create_terrain(**validated_data)
    

class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotModel
        fields = (
            "id",
            "tr_id",
            "target_purity",
        )

    def create(self, validated_data):
        return LotModel.objects.create_lot(**validated_data)

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

    def create(self, validated_data):
        return CropModel.objects.create_crop(**validated_data)

class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestModel
        fields = (
            "id",
            "lt_id",
            "flower",
            "waste",
        )

    def create(self, validated_data):
        return HarvestModel.objects.create_harvest(**validated_data)