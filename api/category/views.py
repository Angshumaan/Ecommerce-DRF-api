from rest_framework import viewsets

from .serializers import CategorySerializer
from .models import Category

# Create your views here.


class CategoryViewset(viewsets.ModelViewSet):
    # ----2 steps we need---
    # 1)this is the query what data we need from the database that is model by getting all values
    # 2) And based on the serializer waht we have wrote like fields name etc hat data wiill be  coverted into json that is CategorySerializer class should be included in second step....go through docs Viewsts
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
