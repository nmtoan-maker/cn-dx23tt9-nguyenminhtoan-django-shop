from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Order, OrderItem

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
@login_required
def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('/cart/')

    order = Order.objects.create(user=request.user)

    for id, quantity in cart.items():
        product = Product.objects.filter(id=id).first()
        if product:
            OrderItem.objects.create(
                order=order,
                product=product,
                price=product.price,
                quantity=quantity
            )

    request.session['cart'] = {}
    request.session.modified = True

    return redirect('my_orders')


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())

    for order in orders:
        total_amount = 0
        items = list(order.orderitem_set.all())

        for item in items:
            item.line_total = item.price * item.quantity
            total_amount += item.line_total

        order.items = items
        order.total_amount = total_amount

    return render(request, 'store/my_orders.html', {
        'orders': orders,
        'cart_count': cart_count,
    })
@login_required
def pay_order(request, order_id):
    order = Order.objects.filter(id=order_id, user=request.user).first()

    if order and order.status == 'pending':
        order.status = 'paid'
        order.save()

    return redirect('my_orders')