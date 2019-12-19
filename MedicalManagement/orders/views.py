from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    if request.session.has_key('user_email'):
        email = request.session['user_email']
        cart = Cart(request)
        if request.method == 'POST':
            try:
                form = OrderCreateForm(request.POST)
                if form.is_valid():
                    order = form.save()
                    for item in cart:
                        OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
                        # clear the cart
                        cart.clear()
                        return render(request, 'orders/order/created.html', {'order': order,'user_email': email})
            except Exception as e:
                print(e)
        else:
            form = OrderCreateForm()
        return render(request, 'orders/order/create.html', {'cart': cart,
                                                            'form': form,'user_email': email})
    else:
        return render(request, "User/login.html")
