from Products.domain.Brand import Brand
from Products.infrastructure.models import BrandModel

class BrandMapper:
    @staticmethod
    def to_domain(brand_model:BrandModel)->Brand:
        return Brand(
            brand_model.name,
            brand_model.countryOrigin,
            brand_model.id
        )