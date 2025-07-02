from products.domain.BrandRepository  import BrandRepository
from products.domain.value_objects.DeleteBrandResult import DeleteBrandResult


class BrandRemover:
    def __init__(self,brandRepository: BrandRepository):
        self.brandRepository = brandRepository

    def delete_brand(self,brand_id: int)->DeleteBrandResult:
        return self.brandRepository.delete_brand(brand_id)