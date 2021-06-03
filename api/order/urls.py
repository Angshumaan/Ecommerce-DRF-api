from rest_framework import routers
from django.urls import path, include
from . import views
# from routers django rest framework
router = routers.DefaultRouter()
router.register(r'', views.OrderViewset)

urlpatterns = [
    path('add/<str:id>/<str:token>/', views.add, name='order.add'),
    path('', include(router.urls))
]
