from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Products
from .forms import ProductsForm


def get_products(request):
    products = Products.objects.all()
    return render(request=request, template_name="show_prod.html", context=dict(products=products))


def add_products(request):
    form = ProductsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("products")
    return render(request=request, template_name="add_prod.html", context=dict(form=form))


def delete_products(request, pk):
    product = Products.objects.filter(pk=pk).first()
    if product:
        product.delete()
        return redirect("products")
    return render(request=request, templates_name="del_prod.html", context=dict(product=product))


def edit_products(request, pk):
    product = Products.objects.filter(pk=pk).first()
    if not product:
        return redirect("products")
    
    if request.method == "POST":
        form = ProductsForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products")
        else:
            form = ProductsForm(instance=product)
    
    return render(request=request, template_name="edit_prod.html", context=dict(product=product))
    