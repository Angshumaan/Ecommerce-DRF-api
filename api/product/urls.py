from rest_framework import routers
from django.urls import path, include
from . import views
# from routers django rest framework
router = routers.DefaultRouter()
# homeroute that is api
router.register(r'', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]
