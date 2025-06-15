from rest_framework import serializers
from Products.domain.Brand import Brand

class BrandSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    countryOrigin = serializers.CharField(max_length=100)

    def to_representation(self, instance):
        if isinstance(instance, Brand):
            return {
                "id": instance.get_id(),
                "name": instance.getName(),
                "countryOrigin": instance.getCountryOrigin()
            }
        return super().to_representation(instance)
