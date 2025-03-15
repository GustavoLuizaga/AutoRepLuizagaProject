from rest_framework import serializers
from Products.domain.Brand import Brand
from Products.domain.Product import Product
from Products.infrastructure.BrandSerializer import BrandSerializer

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=255)
    price = serializers.FloatField()
    stock = serializers.IntegerField()
    description = serializers.CharField()
    reorder = serializers.IntegerField()
    code = serializers.CharField(max_length=100)
    image_url = serializers.CharField()
    brand = BrandSerializer()

    def to_representation(self, instance):
        if isinstance(instance, Product):
            return {
                "id": instance.get_id(),
                "name": instance.get_name(),
                "price": instance.get_price(),
                "stock": instance.get_stock(),
                "description": instance.get_description(),
                "reorder": instance.get_reorder(),
                "code": instance.get_code(),
                "image_url": instance.get_image_url(),
                "brand": BrandSerializer(instance.get_brand()).data
            }
        return super().to_representation(instance)
