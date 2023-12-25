from django.shortcuts import render, get_object_or_404, redirect
from catalog.forms import ProductForm
from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Name: {name}, phone: {phone}, message: {message}')

    return render(request, 'catalog/contacts.html')


def products(request):
    products_list = Product.objects.all()
    context = {
        'products': products_list
    }
    return render(request, 'catalog/products.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')  # Перенаправление на страницу со всеми продуктами
    else:
        form = ProductForm()

    return render(request, 'catalog/create_product.html', {'form': form})