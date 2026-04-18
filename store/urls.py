from django.contrib import admin
from django.urls import path
from store import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list),
    path('product/<int:id>/', views.product_detail),
    path('add-to-cart/<int:id>/', views.add_to_cart),
    path('cart/', views.cart_view),
    path('remove/<int:id>/', views.remove_from_cart),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)