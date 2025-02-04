from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import services
from .forms import *


# Create your views here.

def login_required_decorator(function):
    return login_required(function, login_url='login_page')

@login_required_decorator
def home_dashboard(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    customers = Customer.objects.all()
    orders = Order.objects.all()
    categories_products = []
    table_list = services.get_table()
    print(table_list)
    for category in categories:
        categories_products.append(
            {
                "category": category.name,
                "product": len(Product.objects.filter(category_id=category.id))
            }
        )

    ctx = {
        "counts": {
            "categories": len(categories),
            "products": len(products),
            "customers": len(customers),
            "orders": len(orders),

        },
        "categories_products": categories_products,
        "table_list": table_list,

    }
    return render(request, 'admapp/index.html', ctx)



def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_dashboard')
        else:

            return render(request, 'admapp/login.html', {'error': 'Invalid credentials'})


    return render(request, 'admapp/login.html')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')


@login_required_decorator
def category_list(request):
    categories = Category.objects.all()
    ctx = {'categories': categories}
    return render(request, 'admapp/categories/list.html', ctx)

@login_required_decorator
def category_add(request):
    model = Category()
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('category_list')
    ctx = {
        'form': form,
        'model': model
    }
    return render(request, 'admapp/categories/form.html', ctx)

@login_required_decorator
def category_edit(request, pk):
    model = Category.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('category_list')
    ctx = {
        'form': form,
        'model': model
    }
    return render(request, 'admapp/categories/form.html', ctx)

@login_required_decorator
def delete_category(request, pk):
    model = Category.objects.get(pk=pk)
    model.delete()
    return redirect('category_list')


@login_required_decorator
def product_list(request):
    products = Product.objects.all()
    ctx = {'products': products}
    return render(request, 'admapp/products/list.html', ctx)

@login_required_decorator
def product_add(request):
    model = Product()
    form = ProductForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('product_list')
    ctx = {
        'form': form,
        'model': model
    }
    return render(request, 'admapp/products/form.html', ctx)

@login_required_decorator
def product_edit(request, pk):
    model = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'admapp/products/form.html', {'form': form, 'model': model})

@login_required_decorator
def product_delete(request, pk):
    model = Product.objects.get(pk=pk)
    model.delete()
    return redirect('product_list')


@login_required_decorator
def user_list(request):
    users = Customer.objects.all()
    ctx = {'users': users}
    return render(request, 'admapp/users/list.html', ctx)

@login_required_decorator
def user_add(request):
    model = Customer()
    form = UserForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('user_list')
    ctx = {
        'form': form,
        'model': model

    }
    return render(request, 'admapp/users/form.html', ctx)

@login_required_decorator
def user_edit(request, pk):
    model = Customer.objects.get(pk=pk)
    form = UserForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('user_list')
    ctx = {
        'form': form,
        'model': model
    }
    return render(request, 'admapp/users/form.html', ctx)

@login_required_decorator
def user_delete(request, pk):
    model = Customer.objects.get(pk=pk)
    model.delete()
    return redirect('user_list')


@login_required_decorator
def order_list(request):
    orders = Order.objects.all()
    ctx = {'orders': orders}
    return render(request, 'admapp/order/list.html', ctx)


@login_required_decorator
def customer_order_list(request, id):
    customer_orders = services.get_order_by_user(id=id)
    ctx = {
        'customer_orders': customer_orders
    }
    return render(request, 'admapp/customer_order/list.html', ctx)

@login_required_decorator
def orderproduct_list(request, id):
    productorders = services.get_product_by_order(id=id)
    ctx = {
        'productorders': productorders
    }
    return render(request, 'admapp/product_order/list.html', ctx)










