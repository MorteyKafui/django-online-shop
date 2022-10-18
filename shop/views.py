from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
def product_list(request, category_slug=None):
    catergory = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        catergory = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=catergory)

    context = {"category": catergory, "categories": categories, "products": products}

    return render(request, "shop/product/list.html", context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    return render(request, "shop/product/detail.html", {"product": product})
