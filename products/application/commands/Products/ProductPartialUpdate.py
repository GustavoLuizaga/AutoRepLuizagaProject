from products.domain.ErrorData import NotFoundError
from products.domain.Product import Product
from products.domain.ProductRepository import ProductRepository


class ProductPartialUpdate:
    def __init__(self, product_repository:ProductRepository):
        self._product_repository = product_repository

    def partial_update(self, product_id: int, data_update) -> Product:
        # Add data validation and raise InvalidDataError
        product_response = self._product_repository.partial_update(product_id, data_update)
        if product_response is None:
            raise NotFoundError("Product not found")
        return product_response