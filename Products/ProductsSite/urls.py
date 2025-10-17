from django.urls import path

from . import views


urlpatterns = [
    path("", views.get_products, name="show_prod"),
    path("add_prod/", views.add_products, name="add_prod"),
    path("del_prod/<int:id>", views.delete_products, name="del_prod"),
    path("edit_prod/<int:id>", views.edit_products, name="edit_prod"),
    path("list_view/", views.ProductsView.as_view(), name="list_view")
]