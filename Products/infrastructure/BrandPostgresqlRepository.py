from Products.domain.Brand import Brand
from Products.domain.BrandRepository import BrandRepository
from Products.infrastructure.models import BrandModel

class BrandPostgresqlRepository(BrandRepository):

    def save_brand(self, brand: Brand) ->Brand:
        brandModel = BrandModel( name= brand.getName(), countryOrigin=brand.getCountryOrigin())
        brandModel.save()
        return Brand(brandModel.name, brandModel.countryOrigin,brandModel.id)

    def delete_brand(self, brand_id: int ) ->bool:
        try:
            brandModel = BrandModel.objects.get(id=brand_id)
            brandModel.delete()
            return True
        except BrandModel.DoesNotExist:
            return False

    def update_brand(self, brand: Brand):
        pass

    def get_all_brands(self)-> list[Brand]:
        brandsModel = BrandModel.objects.all()
        brandList = []
        for bran in brandsModel:
            branDomain = Brand(bran.name, bran.countryOrigin, bran.id)
            brandList.append(branDomain)
        return brandList

    def partial_update(self, brand_id: int, data_update) -> Brand:
            brand_model = BrandModel.objects.get(id=brand_id)
            if "name" or "country" in data_update:
                brand_model.name = data_update["name"]
                brand_model.countryOrigin = data_update["countryOrigin"]
                brand_model.save()

            return Brand(brand_model.name, brand_model.countryOrigin,brand_model.id)
