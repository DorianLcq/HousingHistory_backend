from rest_framework import serializers 
from API.models import HousingHistory
 
 
class HousingHistorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = HousingHistory
        fields =['id',
                'postcode',
                'addressLine1',
                'addressLine2', 
                'city', 
                'county',
                'country',
                'movingDate']

