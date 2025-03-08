from . import Brand

class Product:
    def __init__(self, name:str, price:float, stock:int, description:str, reorder:int, code:str,imageUrl:str, brand:Brand):
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__description = description
        self.__reorder = reorder
        self.__code = code
        self.__imageUrl = imageUrl
        self.__brand = Brand

    def getName(self) -> str:
        return self.__name

    def getPrice(self):
        return self.__price

    def getStock(self):
        return self.__stock

    def getDescription(self):
        return self.__description

    def getReorder(self):
        return self.__reorder

    def getCode(self):
        return self.__code

    def getImageUrl(self):
        return self.__imageUrl

    def set_name(self, name:str):
        self.__name = name

    def set_price(self, price:float):
        self.__price = price

    def set_stock(self, stock:int):
        self.__stock = stock

    def set_description(self, description:str):
        self.__description = description

    def set_reorder(self, reorder:int):
        self.__reorder = reorder

    def set_code(self, code:str):
        self.__code = code

    def set_imageUrl(self, imageUrl:str):
        self.__imageUrl = imageUrl