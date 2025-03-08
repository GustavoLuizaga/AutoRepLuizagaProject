from Products.domain.Brand import Brand
from Products.domain.BrandRepository import BrandRepository


class BrandGetAll:
    def __init__(self, brandRepository: BrandRepository):
        self.brandRepository = brandRepository

    def get_all_brands(self) -> list[Brand]:
        return self.brandRepository.get_all_brands()


