from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render
from shopapp.cart import Cart


def car(request):
    user = request.session.get('user')
    cart = request.session.get('cart')
    # print(12, cart.cart_item)

    return render(request, 'car.html', {'user': user, 'cart': cart})


def add_amount(request):
    id = request.GET.get('id')
    value1 = request.GET.get('value')
    if value1.isdigit():
        value1 = int(value1)
    else:
        value1 = 2
    value1 += 1
    cart = request.session.get('cart')
    cart.modify_cart(id, value1)
    request.session['cart'] = cart
    list = [cart.total_price, cart.save_price, value1]
    str = json.dumps(list)
    return HttpResponse(str)


def add_book(request):
    id = request.GET.get('id')
    cart = request.session.get('cart')
    print(37, id)
    if cart is None:
        cart = Cart()
        cart.add_book_toCart(id)
        request.session['cart'] = cart
    else:
        cart.add_book_toCart(id)
        request.session['cart'] = cart
    return HttpResponse('1')



def indent(request):
    user = request.session.get('user')


    return render(request, 'indent.html', {'user': user})



def indent_ok(request):
    user = request.session.get('user')
    return render(request, 'indent ok.html', {'user': user})


