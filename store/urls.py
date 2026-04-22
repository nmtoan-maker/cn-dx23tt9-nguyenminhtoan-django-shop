from django.contrib import admin
from django.urls import path
from store import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.product_list),
    path('product/<int:id>/', views.product_detail),
    path('add-to-cart/<int:id>/', views.add_to_cart),
    path('cart/', views.cart_view),
    path('remove/<int:id>/', views.remove_from_cart),

    path('checkout/', views.checkout, name='checkout'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('pay-order/<int:order_id>/', views.pay_order, name='pay_order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)