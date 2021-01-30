from django.shortcuts import render
from . import models
# Create your views here.


def home(request):
    orders = models.Order.objects.all()
    customers = models.Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()

    delivered__orders = orders.filter(status='Delivered').count()
    pending__orders = orders.filter(status='pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'total_customers': total_customers, 'delivered': delivered__orders, 'pending': pending__orders}

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = models.Product.objects.all()
    return render(request, "accounts/products.html", {
        "products": products,
    })


def customer(request, pk_test):
    customer = models.Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()
    return render(request, "accounts/customer.html", {
        "customer": customer,
        "orders": orders,
        "order_count": order_count,
    })
