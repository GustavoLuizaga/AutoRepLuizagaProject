
from Products.domain.Brand import Brand
from Products.domain.BrandRepository import BrandRepository
from Products.domain.BrandValidatorDataUpdate import BrandValidatorDataUpdate

class BrandPartialUpdate:
    def __init__(self, brand_repository: BrandRepository):
        self.brand_repository = brand_repository

    def partial_update(self, brand_id: int, data_update):
        validator_name = BrandValidatorDataUpdate(data_update)
        if not validator_name.is_valid_name():
            return None
        return self.brand_repository.partial_update(brand_id, data_update)


