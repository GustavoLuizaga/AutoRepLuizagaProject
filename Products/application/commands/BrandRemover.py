from Products.domain.BrandRepository  import BrandRepository
class BrandRemover:
    def __init__(self,brandRepository: BrandRepository):
        self.brandRepository = brandRepository

    def delete_brand(self,brand_id: int)->bool:
        return self.brandRepository.delete_brand(brand_id)
