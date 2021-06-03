from rest_framework import routers
from django.urls import path, include
from . import views
# from routers django rest framework
router = routers.DefaultRouter()
router.register(r'', views.CategoryViewset)

urlpatterns = [
    path('', include(router.urls))
]
