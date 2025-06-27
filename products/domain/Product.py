from . import Brand

class Product:
    def __init__(self, name: str, price: float, stock: int, description: str, reorder: int, code: str, image_url: str, brand: Brand,id:int = None ):
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__description = description
        self.__reorder = reorder
        self.__code = code
        self.__image_url = image_url
        self.__brand = brand
        self.__id = id

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def get_description(self) -> str:
        return self.__description

    def get_reorder(self) -> int:
        return self.__reorder

    def get_code(self) -> str:
        return self.__code

    def get_image_url(self) -> str:
        return self.__image_url

    def get_brand(self) -> Brand:
        return self.__brand

    def set_name(self, name: str):
        self.__name = name

    def set_price(self, price: float):
        self.__price = price

    def set_stock(self, stock: int):
        self.__stock = stock

    def set_description(self, description: str):
        self.__description = description

    def set_reorder(self, reorder: int):
        self.__reorder = reorder

    def set_code(self, code: str):
        self.__code = code

    def set_image_url(self, image_url: str):
        self.__image_url = image_url

    def set_brand(self, brand: Brand):
        self.__brand = brand
