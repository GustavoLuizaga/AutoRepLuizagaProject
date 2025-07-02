
class ProductImage:
    def __init__(self, url_image:str, id_image:int =None):
        self._id = id_image
        self._url_image = url_image

    def get_id_image(self)->int:
        return self._id

    def get_url_image(self)->str:
        return self._url_image

    def set_id_image(self, id_image:int):
        self._id = id_image

    def set_url_image(self, url_image:str):
        self._url_image = url_image
