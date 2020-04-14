from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import HousingHistorySerializer
from .models import HousingHistory
from rest_framework.response import Response

# Create your views here.

class HousingHistoryViewSet(viewsets.ModelViewSet):
    queryset = HousingHistory.objects.all()
    serializer_class = HousingHistorySerializer 
    

