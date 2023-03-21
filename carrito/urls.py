from rest_framework import routers
from .viewset import ProductoViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('Producto', ProductoViewSet)

urlpatterns = router.urls
