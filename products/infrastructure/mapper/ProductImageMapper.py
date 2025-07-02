from products.domain.ProductImage import ProductImage
from products.infrastructure.models import ImageProductModel


class ProductImageMapper:

    @staticmethod
    def to_domain(image_model:list[ImageProductModel])->list[ProductImage]:
        images_domain = [ProductImage(url_image=img.image_url,id_image=img.id) for img in image_model]
        return images_domain
