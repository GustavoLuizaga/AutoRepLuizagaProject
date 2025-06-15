from Products.domain.Product import Product
from Products.domain.ProductRepository import ProductRepository
from Products.infrastructure.models import ProductModel, BrandModel
from Products.infrastructure.Mapper.ProductMapper import ProductMapper


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

    def delete_product(self, product_id:int)->bool:
        try:
            product_model = ProductModel.objects.get(id=product_id)
            product_model.delete()
            return True
        except ProductModel.DoesNotExist:
            return False

    def get_all_products(self)->list[Product]:
        products = ProductModel.objects.all().order_by("id")
        if not products.exists():
            return []
        return [ProductMapper.to_domain(product_model) for product_model in products]
