from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from order.forms import OrderForm
from order.models import Order
from user.models import Profile


@login_required
def profile(request, username):
    user = get_object_or_404(Profile, username=username)
    if request.user != user:
        return render(request, 'order/permission.html')
    if user.status == 'CUSTOMER':
        form = OrderForm(request.POST or None)
        template = 'order/create_order.html'
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            list_order = customer_list_order(request)
            return render(request, 'order/customer_list.html', context={'orders': list_order})
        return render(request, template, context={'form': form, 'user': user})
    orders = Order.objects.filter(
        accepted=False, canceled=False
    ).prefetch_related('customer', 'perfomer').order_by('pub_date')
    all_user_orders = Order.objects.filter(perfomer=user).count()
    accept_user_orders = Order.objects.filter(perfomer=user, accepted=True).count()
    canceled_user_orders = (
        Order.objects.filter(perfomer=user, canceled=True).count()
    )
    context = {
        'all_user_orders': all_user_orders,
        'accept_user_orders': accept_user_orders,
        'canceled_user_orders': canceled_user_orders,
        'orders': orders,
        'user': user
    }
    return render(request, 'order/profile.html', context=context)


def list_orders(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', context={'orders': orders})


def customer_list_order(request):
    orders = Order.objects.filter(customer=request.user)
    return orders


@login_required
def perfomer_list_order(request, username):
    user = get_object_or_404(Profile, username=username)
    if request.user != user:
        return render(request, 'order/permission.html')
    orders = Order.objects.filter(
        perfomer=Profile.objects.get(username=username)
    )
    return render(
        request, 'order/perfomer_list.html', context={'orders': orders}
    )


def accept_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.perfomer = request.user
    order.accepted = True
    order.save()
    return redirect('orders:profile', request.user)


def canceled_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.perfomer = request.user
    order.canceled = True
    order.save()
    return redirect('orders:profile', request.user)
