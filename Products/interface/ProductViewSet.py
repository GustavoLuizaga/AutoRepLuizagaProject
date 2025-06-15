from itertools import product

from rest_framework import viewsets, status
from rest_framework.response import Response
from Products.application.commands.ProductCreator import ProductCreator
from Products.domain.ErrorData import ErrorData
from Products.infrastructure.ProductPostgresqlRepository import ProductPostgresqlRepository
from Products.infrastructure.models import BrandModel
from Products.infrastructure.ProductSerializer import ProductSerializer
from Products.infrastructure.BrandPostgresqlRepository import BrandPostgresqlRepository
from Products.application.commands.ProductRemover import ProductRemover
from Products.application.commands.ProductGetAll import ProductGetAll


class ProductViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_repository = ProductPostgresqlRepository()
        self.brand_repository = BrandPostgresqlRepository()
        self.product_remover = ProductRemover(self.product_repository)
        self.product_creator = ProductCreator(self.product_repository,self.brand_repository)
        self.product_get_all= ProductGetAll(self.product_repository,)


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
            return Response({"error": "Product not Found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, pk=None):
        success = self.product_remover.delete_product(pk)
        if success:
            return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        product_list = self.product_get_all.get_all_products()
        return Response(ProductSerializer(product_list,many=True).data, status=status.HTTP_200_OK)
