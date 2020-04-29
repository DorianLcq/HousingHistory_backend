from rest_framework import viewsets
from rest_framework import permissions
from .serializers import HousingHistorySerializer, UserSerializer, EmailSerializer
from .models import HousingHistory, User, Email
from rest_framework.response import Response
from rest_framework.decorators import api_view



# Create your views here.

class HousingHistoryViewSet(viewsets.ModelViewSet):
    queryset = HousingHistory.objects.all()
    serializer_class = HousingHistorySerializer 
    

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

""" def thisisyourtoken(request) : 
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        save_it form.save(commit=False)
        save_it.save()

        subject = 'URL to see your housing history'
        message = 'Welcome to HousingApp ! /n This is your url to see your housing history : /n/n Yours sincerly,/nCyberratss'
        from_email = settings.EMAIL_HOST_USER
        to_list = [save_it.email, settings.EMAIL_HOST_USER]

        send_mail(subject, message, from_email, to_list, fail_silently = True)
 """

class EmailViewSet(viewsets.ModelViewSet):
    
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
