from django.shortcuts import render, redirect
from .models import Product, Category

def product_list(request):
    category_id = request.GET.get('category')

    categories = Category.objects.all()
    products = Product.objects.all()

    if category_id:
        products = products.filter(category__id=category_id)

    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())

    return render(request, 'store/product_list.html', {
        'products': products,
        'cart_count': cart_count,
        'categories': categories,
        'current_category': category_id,
    })


def add_to_cart(request, id):
    cart = request.session.get('cart', {})

    id = str(id)

    if id in cart:
        cart[id] += 1
    else:
        cart[id] = 1

    request.session['cart'] = cart
    return redirect('/')


def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for id, quantity in cart.items():
        product = Product.objects.filter(id=id).first()
        if product:
            product.quantity = quantity
            product.total_price = product.price * quantity
            total += product.total_price
            products.append(product)

    cart_count = sum(cart.values())

    return render(request, 'store/cart.html', {
        'products': products,
        'total': total,
        'cart_count': cart_count,
    })


def product_detail(request, id):
    product = Product.objects.filter(id=id).first()
    if not product:
        from django.http import Http404
        raise Http404

    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())

    return render(request, 'store/product_detail.html', {
        'product': product,
        'cart_count': cart_count,
    })


def remove_from_cart(request, id):
    cart = request.session.get('cart', {})

    id = str(id)

    if id in cart:
        del cart[id]

    request.session['cart'] = cart
    return redirect('/cart/')