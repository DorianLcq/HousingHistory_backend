from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from API import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'housinghistory', views.HousingHistoryViewSet)
router.register(r'emails', views.EmailViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]