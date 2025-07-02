from products.domain.ProductRepository import ProductRepository


class DeleteProductImage:
    def __init__(self, repository:ProductRepository):
        self._repository = repository

    def delete_image_product(self, image_id:int)->bool:
        return self._repository.delete_image_product(image_id)