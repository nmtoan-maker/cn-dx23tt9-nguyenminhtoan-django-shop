from django.urls import path
from .views import product_list, product_detail, import_csv

urlpatterns = [
    path('', product_list),
    path('product/<int:id>/', product_detail),
    path('import-csv/', import_csv),  # 🔥 thêm dòng này
]