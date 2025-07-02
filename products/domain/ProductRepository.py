from abc import ABC, abstractmethod
from products.domain.Product import Product


class ProductRepository(ABC):

    @abstractmethod
    def save_product(self, product:Product):
        pass

    @abstractmethod
    def delete_product(self, product_id:int)->bool:
        pass

    @abstractmethod
    def get_all_products(self)->list[Product]:
        pass

    @abstractmethod
    def partial_update(self, product_id:int, data_update) -> Product:
        pass

    @abstractmethod
    def update_image_product(self, product_id:int,image_id:int, data_update) -> str:
        pass

    @abstractmethod
    def add_product_image(self, product_id:int, image_url:str) -> bool:
        pass
