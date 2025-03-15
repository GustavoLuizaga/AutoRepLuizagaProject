from Products.domain.ErrorData import ErrorData
from Products.domain.Product import Product
from Products.domain.ProductRepository import ProductRepository
from Products.domain.BrandRepository import BrandRepository


class ProductCreator:
    def __init__(self, product_repository: ProductRepository, brand_repository: BrandRepository):
        self.product_repository = product_repository
        self.brand_repository = brand_repository

    def create_product(self,name:str, price:float, stock:int, description:str, reorder:int, code:str,image_url:str,brand_id:int)->Product:
        brand_domain = self.brand_repository.find_brand_by_id(brand_id)
        #Controlar que brand_domain no sea null o si exista
        if brand_domain is None:
            raise ErrorData()
        product = Product(name, price, stock, description, reorder, code, image_url, brand_domain)
        return self.product_repository.save_product(product)

