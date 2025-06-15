from Products.domain.BrandRepository import BrandRepository
from Products.domain.Brand import Brand

class BrandCreator:
    def __init__(self, brandRepository: BrandRepository):
        self.brandRepository = brandRepository

    def create_brand(self,name: str, country_origin: str) -> Brand:
        brand = Brand(name, country_origin)
        return self.brandRepository.save_brand(brand)
