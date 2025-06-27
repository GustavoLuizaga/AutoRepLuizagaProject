from products.domain.ProductRepository import ProductRepository

class ProductGetAll:
    def __init__(self,product_repository: ProductRepository):
        self.__product_repository = product_repository

    def get_all_products(self):
        return self.__product_repository. get_all_products()