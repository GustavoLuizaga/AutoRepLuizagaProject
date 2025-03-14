from Products.domain.Brand import Brand
from Products.domain.BrandRepository import BrandRepository
from Products.domain.BrandValidatorDataUpdate import BrandValidatorDataUpdate
class BrandFindByName:
    def __init__(self, brand_repository: BrandRepository):
        self.repository = brand_repository

    def find_brand_by_name(self, name: str)-> Brand:
        return self.repository.find_brand_by_name(name)

