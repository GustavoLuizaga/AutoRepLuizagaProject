
from products.domain.Brand import Brand
from products.domain.BrandRepository import BrandRepository
from products.domain.BrandValidatorDataUpdate import BrandValidatorDataUpdate
from products.domain.ErrorData import ErrorData


class BrandPartialUpdate:
    def __init__(self, brand_repository: BrandRepository):
        self.brand_repository = brand_repository

    def partial_update(self, brand_id: int, data_update) -> Brand:
        validator_name = BrandValidatorDataUpdate(data_update)
        if not validator_name.is_valid_name():
            raise ErrorData()
        return self.brand_repository.partial_update(brand_id, data_update)


