from Products.domain.Product import Product
from Products.domain.ProductRepository import ProductRepository


class ProductCreator:
    def __init__(self, productRepository: ProductRepository):
        self.productRepository = productRepository

    def create_product(self,name:str, price:float, stock:int, description:str, reorder:int, code:str,imageUrl:str):

        porduct = Product(name, price, stock, description, reorder, code, imageUrl);

