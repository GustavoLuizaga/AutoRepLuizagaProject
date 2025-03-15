from abc import ABC, abstractmethod
from . import Brand

class BrandRepository(ABC):
    @abstractmethod
    def save_brand(self, brand: Brand):
        pass

    @abstractmethod
    def delete_brand(self, brand_id: int ):
        pass

    @abstractmethod
    def update_brand(self, brand_id: int ):
        pass

    @abstractmethod
    def get_all_brands(self):
        pass

    @abstractmethod
    def partial_update(self, brand_id: int, data_update) -> Brand:
        pass

    @abstractmethod
    def find_brand_by_name(self, brand_name: str)-> Brand:
        pass

    @abstractmethod
    def find_brand_by_id(self, id_brand: int) -> Brand:
        pass