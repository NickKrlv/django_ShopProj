from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.views import home, contacts, products, product_detail
from catalog.views import create_product

urlpatterns = [
                  path('', home, name='home'),
                  path('contacts/', contacts, name='contacts'),
                  path('products/', products, name='products'),
                  path('product/<int:product_id>/', product_detail, name='product_detail'),
                  path('create_product/', create_product, name='create_product'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
