from products.domain.ProductRepository import ProductRepository


class ProductImageUpdate:
    def __init__(self, repository:ProductRepository):
        self._repository = repository

    def update_image_product(self, product_id:int,image_id:int, data_update) -> str:
        return self._repository.update_image_product(product_id, image_id, data_update)

