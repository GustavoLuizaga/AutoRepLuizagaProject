from products.domain.Product import Product
from products.infrastructure.models import ProductModel
from products.infrastructure.mapper.BrandMapper import BrandMapper
from products.infrastructure.mapper.ProductImageMapper import ProductImageMapper

class ProductMapper:
    @staticmethod
    def to_domain(product_model:ProductModel)->Product:
        image_urls_models = product_model.images_product.all()
        return Product(
            id=product_model.id,
            code=product_model.code,
            name=product_model.name,
            price=product_model.price,
            stock=product_model.stock,
            description=product_model.description,
            image_url=ProductImageMapper.to_domain(list(image_urls_models)),
            reorder=product_model.reorder,
            brand=BrandMapper.to_domain(product_model.brand)
        )