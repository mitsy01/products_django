from django import forms 

from .models import Products


class ProductsForm(forms.ModelForm):
    name_prod = forms.CharField(
        max_length=100,
        label="Назва товару",
        widget=forms.TextInput(attrs={"class": "form-control"})
)
    price = forms.IntegerField(
        label="Ціна товару",
        widget=forms.NumberInput(attrs={"class": "form-control"})
)
    description = forms.CharField(
        max_length=500,
        label="Опис товару",
        widget=forms.TextInput(attrs={"class": "form-control"})
)
    expiration_date = forms.DateField(
        label="Строк придатності товару",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"})
    )
    
    class Meta:
        fields = ["name_prod", "price", "description", "expiration_date",]