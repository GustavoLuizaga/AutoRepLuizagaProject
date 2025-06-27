'''

from django.urls import path
from products.interface.BrandCreateView import BrandCreateView
from products.interface.BrandDeleteView import BrandDeleteView
from products.interface.BrandGetAllView import BrandGetAllView

urlpatterns = [
    path('brand/', BrandCreateView.as_view()),
    path('brand/<int:brand_id>/', BrandDeleteView.as_view()),
    path('brand2/', BrandGetAllView.as_view()),


]
'''

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.interface.BrandViewSet import BrandViewSet
from products.interface.ProductViewSet import ProductViewSet

router = DefaultRouter()
router.register(r'brand', BrandViewSet, basename='brand')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),

]
