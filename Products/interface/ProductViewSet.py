from rest_framework import viewsets, status
from rest_framework import viewsets
from rest_framework.response import Response
from Products.application.commands.ProductCreator import ProductCreator
from Products.domain.Brand import Brand
from Products.domain.ErrorData import ErrorData
from Products.infrastructure.ProductPostgresqlRepository import ProductPostgresqlRepository
from Products.infrastructure.models import BrandModel
from Products.infrastructure.ProductSerializer import ProductSerializer
from Products.infrastructure.BrandPostgresqlRepository import BrandPostgresqlRepository


class ProductViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_repository = ProductPostgresqlRepository()
        self.brand_repository = BrandPostgresqlRepository()
        self.product_creator = ProductCreator(self.product_repository,self.brand_repository)

    def create(self, request):
        try:
            product = self.product_creator.create_product(
                request.data.get('name'),
                request.data.get('price'),
                request.data.get('stock'),
                request.data.get('description'),
                request.data.get('reorder'),
                request.data.get('code'),
                request.data.get('image_url'),
                request.data.get('brand_id'))
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        except ErrorData:
            return Response({"error": "Brand Not Found"}, status=status.HTTP_404_NOT_FOUND)
