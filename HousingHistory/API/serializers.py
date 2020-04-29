from rest_framework import serializers 
from API.models import HousingHistory, User, Email
import re
from ukpostcodeutils import validation
from HousingHistory import settings
from django.core.mail import send_mail




class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'token']

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
                'movingDate',
                'user']

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

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['to_email','subject', 'message']

    def sendEmail(self, value) :
        send_mail(value.subject, value.message, settings.EMAIL_HOST_USER, [value.to_email,], fail_silently=False)

    def create(self, validated_data):
        value = super().create(validated_data)
        self.sendEmail(value)
        return value
