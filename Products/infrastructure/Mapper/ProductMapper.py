from Products.domain.Product import Product
from Products.infrastructure.models import ProductModel
from Products.infrastructure.Mapper.BrandMapper import BrandMapper

class ProductMapper:
    #No es necesario instanciar esta clase por eso se usa la notacion
    @staticmethod
    def to_domain(product_model:ProductModel)->Product:
        return Product(
            id=product_model.id,
            code=product_model.code,
            name=product_model.name,
            price=product_model.price,
            stock=product_model.stock,
            description=product_model.description,
            image_url=product_model.image,
            reorder=product_model.reorder,
            brand=BrandMapper.to_domain(product_model.brand)
        )