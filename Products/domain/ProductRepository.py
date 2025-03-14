from abc import ABC, abstractmethod
from Products.domain.Product import Product


class ProductRepository(ABC):

    @abstractmethod
    def save_product(self, product:Product):
        pass

    @abstractmethod
    def update_product(self, product:Product):
        pass

    @abstractmethod
    def delete_product(self, product:Product):
        pass

    @abstractmethod
    def get_all_products(self) -> list[Product]:
        pass

    @abstractmethod
    def find_by_idProduct(self, idProduct:int) -> Product:
        pass

    @abstractmethod
    def search_by_nameProduct(self, nameProduct:str) -> list[Product]:
        pass



