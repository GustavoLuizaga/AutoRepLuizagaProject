'''

from django.urls import path
from Products.interface.BrandCreateView import BrandCreateView
from Products.interface.BrandDeleteView import BrandDeleteView
from Products.interface.BrandGetAllView import BrandGetAllView

urlpatterns = [
    path('brand/', BrandCreateView.as_view()),
    path('brand/<int:brand_id>/', BrandDeleteView.as_view()),
    path('brand2/', BrandGetAllView.as_view()),


]
'''

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Products.interface.BrandViewSet import BrandViewSet
from Products.interface.ProductViewSet import ProductViewSet

router = DefaultRouter()
router.register(r'brand', BrandViewSet, basename='brand')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),

]
