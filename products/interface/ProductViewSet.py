from rest_framework import viewsets, status
from rest_framework.response import Response

from products.application.commands.Products.AddProductImage import AddProductImage
from products.application.commands.Products.ProductCreator import ProductCreator
from products.application.commands.Products.ProductImageUpdate import ProductImageUpdate
from products.application.commands.Products.ProductPartialUpdate import ProductPartialUpdate
from products.domain.ErrorData import ErrorData, NotFoundError, InvalidDataError
from products.infrastructure.repository.ProductPostgresqlRepository import ProductPostgresqlRepository
from products.infrastructure.serializer.ProductSerializer import ProductSerializer
from products.infrastructure.repository.BrandPostgresqlRepository import BrandPostgresqlRepository
from products.application.commands.Products.ProductRemover import ProductRemover
from products.application.commands.Products.ProductGetAll import ProductGetAll
from rest_framework.decorators import action


class ProductViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_repository = ProductPostgresqlRepository()
        self.brand_repository = BrandPostgresqlRepository()
        self.product_remover = ProductRemover(self.product_repository)
        self.product_creator = ProductCreator(self.product_repository,self.brand_repository)
        self.product_partial_update = ProductPartialUpdate(self.product_repository)
        self.product_get_all= ProductGetAll(self.product_repository)
        self.add_product_image = AddProductImage(self.product_repository)
        self.product_image_update = ProductImageUpdate(self.product_repository)


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
            return Response({"error": "Brand not Found"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request, pk=None):
        success_destroy = self.product_remover.delete_product(pk)
        if success_destroy:
            return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    def list(self,request):
        product_list = self.product_get_all.get_all_products()
        return Response(ProductSerializer(product_list,many=True).data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        data = request.data
        try:
            product_update = self.product_partial_update.partial_update(pk, data)
            return  Response(ProductSerializer(product_update).data, status=status.HTTP_200_OK)
        except NotFoundError as e:
                return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except InvalidDataError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['patch'], url_path=r'(?P<product_id>\d+)/(?P<image_id>\d+)/update-image')
    def update_image(self, request, product_id=None, image_id=None):
        success_update = self.product_image_update.update_image_product(product_id, image_id, request.data.get('image_url'))
        return Response({"detail":success_update}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'], url_path='add-image')
    def add_image(self, request, pk=None):
        success_add = self.add_product_image.add_product_image(pk, request.data.get('image_url'))
        if success_add:
            return Response({"message": "Image added successfully"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Image not added"}, status=status.HTTP_400_BAD_REQUEST)
