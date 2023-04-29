from django.contrib import admin
from django.urls import path, include
from utsApiApp.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jadwal_SumbawaBesar', jadwalViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
