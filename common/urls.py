from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('admin-region', AdminRegionViewSet, basename='admin-region')

urlpatterns = [
    path('api/', include(router.urls)),
]