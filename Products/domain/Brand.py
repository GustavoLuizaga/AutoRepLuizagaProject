
class Brand:
    def __init__(self,name:str, countryOrigin:str, id:int = None ):
        self.__idBrand = id
        self.__name = name
        self.__countryOrigin = countryOrigin

    def get_id(self):
        return self.__idBrand

    def getName(self) -> str:
        return self.__name

    def getCountryOrigin(self) -> str:
        return self.__countryOrigin

    def setName(self, name:str):
        self.__name = name

    def setCountryOrigin(self, countryOrigin:str):
        self.__countryOrigin = countryOrigin

    def setId(self, idBrand:int):
        self.__idBrand = idBrand

