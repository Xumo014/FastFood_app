from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .forms import *
from .services import *
from .models import *
from django.http import JsonResponse
import json
from Maxwaypractic.settings import MEDIA_ROOT


# Create your views here.

def home_page(request):
    if request.GET:
        product = get_product_by_id(request.GET.get("product_id", 0))
        return JsonResponse(product)


def order_page(request):
    user = get_user_by_phone(request.GET.get("phone", 0))
    return JsonResponse(user)


def index_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    orders = []
    orders_list = request.COOKIES.get("orders")
    total_price = request.COOKIES.get("total_price", 0)
    print(orders_list)
    print(total_price)
    if orders_list:
        for key, val in json.loads(orders_list).items():
            try:
                product = Product.objects.get(pk=int(key))
                orders.append(
                    {
                        "product": product,
                        "count": val
                    }
                )
            except ObjectDoesNotExist:
                print(f"Product with ID {key} does not exist in the database.")
    ctx = {
        'categories': categories,
        'products': products,
        'orders': orders,
        'total_price': total_price,
        'MEDIA_ROOT': MEDIA_ROOT
    }

    response = render(request, 'food/index.html', ctx)
    return response


def main_order(request):
    model = Customer()
    print(request.POST.get("phone"))
    if request.POST:
        try:
            model = Customer.objects.get(phone=request.POST.get("phone", ""))
            print("model", model)

        except:
            model = Customer()
        form = CustomerForm(request.POST or None, instance=model)
        if form.is_valid():
            customer = form.save()
            formor = OrderForm(request.POST or None, instance=Order())
            if formor.is_valid():
                order = formor.save(customer=customer)
                print("order:", order)
                orders_list = request.COOKIES.get("orders")
                print("order_list", orders_list)

                for key, value in json.loads(orders_list).items():
                    product = get_product_by_id(int(key))
                    counts = value
                    order_product = OrderProduct(
                        count=counts,
                        price=product['price'],
                        product_id=product['id'],
                        order_id=order.id
                    )
                    order_product.save()

                return redirect("index")
            else:
                print(formor.errors)
        else:
            print(form.errors)

    categories = Category.objects.all()
    products = Product.objects.all()
    orders = []
    order_list = request.COOKIES.get("orders")
    total_price = request.COOKIES.get("total_price", 0)

    if order_list:
        try:
            orders_data = json.loads(order_list)
            for key, val in orders_data.items():
                try:
                    product = Product.objects.get(pk=key)
                    orders.append(
                        {
                            "product": product,
                            "count": val
                        }
                    )
                except Product.DoesNotExist:
                    continue
        except json.JSONDecodeError:
            orders = []

    ctx = {
        "categories": categories,
        "products": products,
        "orders": orders,
        "total_price": total_price,
        "MEDIA_ROOT": MEDIA_ROOT
    }

    response = render(request, 'food/order.html', ctx)
    return response
