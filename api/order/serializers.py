from rest_framework import serializers

from .models import Order

# Serialization is for converting into json


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Category will be converted into json
        model = Order
        # which one you want to modify
        fields = ('user', 'product_names', 'total_products',
                  'transaction_id', 'total_amount')
