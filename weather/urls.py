from django.urls import include, path
from rest_framework.routers import DefaultRouter
from weather.views import AdminRegionViewSet

router = DefaultRouter()
router.register('admin-region', AdminRegionViewSet, basename='admin-region')

urlpatterns = [
    path('api/', include(router.urls)),
]