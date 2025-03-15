from Products.domain.Brand import Brand
from Products.domain.BrandRepository import BrandRepository


class BrandFindById:
    def __init__(self,brand_repository: BrandRepository):
        self.brand_repository = brand_repository

    def find_brand_by_id(self, id_brand: int) -> Brand:
        return self.brand_repository.find_brand_by_id(id_brand)
