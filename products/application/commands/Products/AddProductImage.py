from products.domain.ProductRepository import ProductRepository


class AddProductImage:
    def __init__(self, repository:ProductRepository):
        self._repository = repository

    def add_product_image(self, product_id:int, image_url:str) -> bool:
        return self._repository.add_product_image(product_id, image_url)