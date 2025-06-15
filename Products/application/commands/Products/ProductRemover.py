from Products.domain.ProductRepository import ProductRepository

class ProductRemover:
    def __init__(self, product_repository: ProductRepository):
        self.__product_repository = product_repository

    def delete_product(self,product_id:int):
        return self.__product_repository.delete_product(product_id)
