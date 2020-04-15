from rest_framework import serializers 
from API.models import HousingHistory
import re
from ukpostcodeutils import validation
 
 
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

    def validate_postcode(self,value):
        postcode = re.findall("^[A-Za-z0-9 ]{5,8}$",value)
        if postcode:
            postcode = value.upper().replace(" ","")        # Convert to uppercase and remove the spaces
            if validation.is_valid_postcode(postcode):      # Check if the postcode exists, to use it you need to import  from ukpostcodeutils import validation
                return postcode
            else:
                raise serializers.ValidationError('This postcode does not exist')
        else:
            raise serializers.ValidationError("Remember, the length of the postcode must be between 5-8 and it can not contain special character(/?*...) ")
