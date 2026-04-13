import csv
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product


def product_list(request):
    keyword = request.GET.get('q')
    category = request.GET.get('category')

    products = Product.objects.all()

    if keyword:
        products = products.filter(name__icontains=keyword)

    if category:
        products = products.filter(category=category)

    return render(request, 'store/product_list.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/product_detail.html', {'product': product})


def import_csv(request):
    file_path = 'products.csv'

    Product.objects.all().delete()

    with open(file_path, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            try:
                Product.objects.create(
                    name=row[0],
                    price=int(row[1]),
                    description=row[2],
                    category='laptop'  # mặc định
                )
            except:
                continue

    return HttpResponse("Import thành công!")