from rest_framework import serializers

from .models import Category

# Serialization is for converting into json


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Category will be converted into json
        model = Category
        # which one you want to modify
        fields = ('name', 'description')
