from products.domain.Product import Product
from products.domain.ProductRepository import ProductRepository
from products.infrastructure.models import ImageProductModel
from products.infrastructure.models.BrandModel import BrandModel
from products.infrastructure.models.ProductModel import ProductModel
from products.infrastructure.mapper.ProductMapper import ProductMapper


class ProductPostgresqlRepository(ProductRepository):

    def save_product(self, product: Product) -> Product:
        brand_model = BrandModel.objects.get(id=product.get_brand().get_id())
        product_model = ProductModel.objects.create(
            code=product.get_code(),
            name=product.get_name(),
            price=product.get_price(),
            stock=product.get_stock(),
            description=product.get_description(),
            reorder=product.get_reorder(),
            brand=brand_model
        )
        ImageProductModel.objects.bulk_create([
            ImageProductModel(product=product_model, image_url=url)
            for url in product.get_image_url()
        ])

        image_urls = [img.image_url for img in product_model.images_product.all()]
        return Product(
            id=product_model.id,
            code=product_model.code,
            name=product_model.name,
            price=product_model.price,
            stock=product_model.stock,
            description=product_model.description,
            reorder=product_model.reorder,
            image_url=image_urls,
            brand=product.get_brand()
        )
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

    def partial_update(self, product_id: int, data_update) -> Product:
        try:
            product_model = ProductModel.objects.get(id=product_id)

            if "name" in data_update:
                product_model.name = data_update["name"]

            if "price" in data_update:
                product_model.price = data_update["price"]

            if "stock" in data_update:
                product_model.stock = data_update["stock"]

            if "description" in data_update:
                product_model.description = data_update["description"]

            if "reorder" in data_update:
                product_model.reorder = data_update["reorder"]

            if "code" in data_update:
                product_model.code = data_update["code"]

            if "image" in data_update:
                product_model.image = data_update["image"]

            if "brand" in data_update:
                product_model.brand = data_update["brand"]

            product_model.save()
            return ProductMapper.to_domain(product_model)

        except ProductModel.DoesNotExist:
            return None


