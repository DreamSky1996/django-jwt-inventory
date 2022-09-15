from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "data", "del_flag")
    
    def update(self, instance, validated_data):
        instance.data = validated_data.get("data", instance.data)
        instance.del_flag = validated_data.get("del_flag", instance.del_flag)
        instance.save()
        return instance