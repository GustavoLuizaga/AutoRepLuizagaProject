from products.domain.ErrorData import ErrorData
from products.domain.Product import Product
from products.domain.ProductImage import ProductImage
from products.domain.ProductRepository import ProductRepository
from products.domain.BrandRepository import BrandRepository


class ProductCreator:
    def __init__(self, product_repository: ProductRepository, brand_repository: BrandRepository):
        self.product_repository = product_repository
        self.brand_repository = brand_repository

    def create_product(self,name:str, price:float, stock:int, description:str, reorder:int, code:str,image_url:list[str],brand_id:int)->Product:
        brand_domain = self.brand_repository.find_brand_by_id(brand_id)
        if brand_domain is None:
            raise ErrorData()
        images = [ProductImage(url_image=url) for url in image_url] if image_url else []
        product = Product(name, price, stock, description, reorder, code, images, brand_domain)
        return self.product_repository.save_product(product)

