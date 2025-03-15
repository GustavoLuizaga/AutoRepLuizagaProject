from Products.domain.Product import Product
from Products.domain.ProductRepository import ProductRepository
from Products.infrastructure.models import ProductModel, BrandModel


class ProductPostgresqlRepository(ProductRepository):

    def save_product(self, product:Product)->Product:
        brand = product.get_brand()
        brand_model = BrandModel.objects.get(id=brand.get_id())
        product_model = ProductModel(
            stock=product.get_stock(),
            code=product.get_code(),
            name=product.get_name(),
            price=product.get_price(),
            description=product.get_description(),
            image=product.get_image_url(),
            reorder=product.get_reorder(),
            brand=brand_model)
        product_model.save()
        return Product(product_model.name, product_model.price, product_model.stock, product_model.description, product_model.reorder,product_model.code, product_model.image,product_model.brand,product_model.id)

