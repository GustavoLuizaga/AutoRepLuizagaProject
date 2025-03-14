from rest_framework import viewsets, status
from rest_framework.response import Response
from Products.application.commands.BrandCreator import BrandCreator
from Products.application.commands.BrandRemover import BrandRemover
from Products.application.commands.BrandGetAll import BrandGetAll
from Products.application.commands.BrandPartialUpdate import BrandPartialUpdate
from Products.infrastructure.BrandPostgresqlRepository import BrandPostgresqlRepository
from Products.infrastructure.BrandSerializer import BrandSerializer

class BrandViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = BrandPostgresqlRepository()
        self.brand_creator = BrandCreator(self.repository)
        self.brand_remover = BrandRemover(self.repository)
        self.brand_get_all = BrandGetAll(self.repository)
        self.brand_partial_update = BrandPartialUpdate(self.repository)

    def list(self, request):
        """GET /brand/ - Obtener todas las marcas"""
        brand_list = self.brand_get_all.get_all_brands()
        return Response(BrandSerializer(brand_list, many=True).data, status=status.HTTP_200_OK)

    def create(self, request):
        """POST /brand/ - Crear una nueva marca"""
        name = request.data.get('name')
        country_origin = request.data.get('countryOrigin')
        if not name or not country_origin:
            return Response({"error": "Both 'name' and 'countryOrigin' are required."},
                            status=status.HTTP_400_BAD_REQUEST)
        brand = self.brand_creator.create_brand(name, country_origin)
        return Response(BrandSerializer(brand).data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        """DELETE /brand/{id}/ - Eliminar una marca por ID"""
        success = self.brand_remover.delete_brand(pk)
        if success:
            return Response({"message": "Brand deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Brand not found"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        data = request.data
        update_brand = self.brand_partial_update.partial_update(pk, data)
        if update_brand is None:
            return Response({"error": "The 'name' attribute cannot be empty"}, status=status.HTTP_404_NOT_FOUND)
        return Response(BrandSerializer(update_brand).data, status=status.HTTP_200_OK)

