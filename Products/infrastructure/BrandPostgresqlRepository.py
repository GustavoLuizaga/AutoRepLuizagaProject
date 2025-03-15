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
        brandsModel = BrandModel.objects.all().order_by("id")
        brandList = []
        for bran in brandsModel:
            branDomain = Brand(bran.name, bran.countryOrigin, bran.id)
            brandList.append(branDomain)
        return brandList

    def partial_update(self, brand_id: int, data_update) -> Brand:
            try:
                brand_model = BrandModel.objects.get(id=brand_id)
                if "name" in data_update:
                    brand_model.name = data_update["name"]
                    brand_model.save()
                if  "countryOrigin" in data_update:
                    brand_model.countryOrigin = data_update["countryOrigin"]
                    brand_model.save()

                return Brand(brand_model.name, brand_model.countryOrigin,brand_model.id)
            except BrandModel.DoesNotExist:
                return None

    def find_brand_by_name(self, name) -> Brand:
        brand_model = BrandModel.objects.filter(name__iexact=name).first()
        if not brand_model:
            return None
        return Brand(brand_model.name, brand_model.countryOrigin, brand_model.id)

    def find_brand_by_id(self, brand_id) -> Brand:
        try:
            brand_model = BrandModel.objects.get(id=brand_id)
            return Brand(brand_model.name, brand_model.countryOrigin, brand_model.id)
        except BrandModel.DoesNotExist:
            return None
