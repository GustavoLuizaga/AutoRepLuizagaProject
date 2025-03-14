from Products.domain.Product import Product
from Products.domain.ProductRepository import ProductRepository


class ProductCreator:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = ProductRepository()

    def create_product(self,name:str, price:float, stock:int, description:str, reorder:int, code:str,image_url:str):
        return self.product_repository.save_product(name, price, stock, description, reorder, code, image_url);

