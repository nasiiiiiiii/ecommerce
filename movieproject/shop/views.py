from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# Create your views here.
def allProCat(request, cat_slug=None):
    cat_page = None
    products_list = None
    if cat_slug!=None:
        cat_page = get_object_or_404(Category, slug=cat_slug)
        #showing 404 page if cat_page is not present
        products_list = Product.objects.all().filter(category=cat_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    my_paginator = Paginator(products_list, 3)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = my_paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = my_paginator.page(my_paginator.num_pages)
    return render(request, "category.html", {'cat_key': cat_page, 'pro_key': products})
def productDetail(request,cat_slug,pro_slug):
    try:
        product = Product.objects.get(category__slug=cat_slug, slug=pro_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html',{'product':product})