from abc import ABC, abstractmethod
from Products.domain.Product import Product


class ProductRepository(ABC):

    @abstractmethod
    def save_product(self, product:Product):
        pass
