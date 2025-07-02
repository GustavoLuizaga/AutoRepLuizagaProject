from rest_framework import serializers
from products.domain.ProductImage import ProductImage

class ProductImageSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    url_image = serializers.CharField(max_length=500)

    def to_representation(self, instance):
        if isinstance(instance, ProductImage):
            return {
            "id": instance.get_id_image(),
            "url_image": instance.get_url_image()
            }
        return super().to_representation(instance)