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
        return redirect("show_prod")
    return render(request=request, template_name="add_prod.html", context=dict(form=form))


def delete_products(request, id):
    try:
        product = Products.objects.get(id=id)
    except Products.DoesNotExist:
        messages.error(request, "Товар не знайдено.")
        return redirect("show_prod")

    if request.method == 'POST':
        product.delete()
        return redirect("show_prod")

    return render(request, "del_prod.html", {"product": product})


    
def edit_products(request, id):
    try:
        product = Products.objects.get(id=id)
    except Products.DoesNotExist:
        messages.error(request, "Товар не знайдено.")
        return redirect("show_prod")

    if request.method == 'POST':
        form = ProductsForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("show_prod")
    else:
        form = ProductsForm(instance=product)

    return render(request, "edit_prod.html", {"form": form, "product": product})