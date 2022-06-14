from production.models import SeedModel, TerrainModel, LotModel, CropModel, HarvestModel
from production.serializers import SeedSerializer, TerrainSerializer, LotSerializer, CropSerializer, HarvestSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions

class SeedAPIView(GenericAPIView):
    serializer_class = SeedSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_list(self):
        """Used to get all the stored seeds basic info"""
        seeds = SeedModel.objects.all()
        return seeds

    def get(self, request):
        seed_id = request.query_params.get("id",None)
        if seed_id != None:
            seed= SeedModel.objects.get(id=seed_id)
            serializer= self.serializer_class(seed)
        else:
            seed= self.get_list()
            serializer= self.serializer_class(seed, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = SeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        seed_id = request.query_params.get("id", None)
        seed = SeedModel.objects.get(id=seed_id)
        serializer = SeedSerializer(seed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        seed_id = request.query_params.get("id", None)
        seed = SeedModel.objects.get(id=seed_id)
        seed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TerrainAPIView(GenericAPIView):
    serializer_class = TerrainSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_list(self):
        """Used to get all the stored terrains basic info"""
        terrain = TerrainModel.objects.all()
        return terrain
    
    def get(self, request):
        terrain_id = request.query_params.get("id",None)
        if terrain_id != None:
            terrain= TerrainModel.objects.get(id=terrain_id)
            serializer= self.serializer_class(terrain)
        else:
            terrain= self.get_list()
            serializer= self.serializer_class(terrain, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TerrainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        terrain_id = request.query_params.get("id", None)
        terrain = TerrainModel.objects.get(id=terrain_id)
        serializer = TerrainSerializer(terrain, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        terrain_id = request.query_params.get("id", None)
        terrain = TerrainModel.objects.get(id=terrain_id)
        terrain.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class LotAPIView(GenericAPIView):
    serializer_class = LotSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_list(self):
        """Used to get all the stored lots basic info"""
        lot = LotModel.objects.all()
        return lot
    
    def get(self, request):
        lot_id = request.query_params.get("id",None)
        if lot_id != None:
            lot= LotModel.objects.get(id=lot_id)
            serializer= self.serializer_class(lot)
        else:
            lot= self.get_list()
            serializer= self.serializer_class(lot, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = LotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        lot_id = request.query_params.get("id", None)
        lot = LotModel.objects.get(id=lot_id)
        serializer = LotSerializer(lot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        lot_id = request.query_params.get("id", None)
        lot = LotModel.objects.get(id=lot_id)
        lot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CropAPIView(GenericAPIView):
    serializer_class = CropSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_list(self):
        """Used to get all the stored crops basic info"""
        crop = CropModel.objects.all()
        return crop
    
    def get(self, request):
        crop_id = request.query_params.get("id",None)
        if crop_id != None:
            crop= CropModel.objects.get(id=crop_id)
            serializer= self.serializer_class(crop)
        else:
            crop= self.get_list()
            serializer= self.serializer_class(crop, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CropSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        crop_id = request.query_params.get("id", None)
        crop = CropModel.objects.get(id=crop_id)
        serializer = CropSerializer(crop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        crop_id = request.query_params.get("id", None)
        crop = CropModel.objects.get(id=crop_id)
        crop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HarvestAPIView(GenericAPIView):
    serializer_class = HarvestSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_list(self):
        """Used to get all the stored harvest basic info"""
        harvest = HarvestModel.objects.all()
        return harvest
    
    def get(self, request):
        harvest_id = request.query_params.get("id",None)
        if harvest_id != None:
            harvest= HarvestModel.objects.get(id=harvest_id)
            serializer= self.serializer_class(harvest)
        else:
            harvest= self.get_list()
            serializer= self.serializer_class(harvest, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = HarvestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        harvest_id = request.query_params.get("id", None)
        harvest = HarvestModel.objects.get(id=harvest_id)
        serializer = HarvestSerializer(harvest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        harvest_id = request.query_params.get("id", None)
        harvest = HarvestModel.objects.get(id=harvest_id)
        harvest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
