from django.db import models
from datetime import datetime

# Create your models here.

class Products(models.Model):
    name_prod = models.CharField(max_length=100, null=True, blank=True, default=None)
    price = models.IntegerField(null=True, blank=True, default=None)
    description = models.CharField(max_length=500, null=True, blank=True, default=None)
    expiration_date = models.DateTimeField()
    
    
    def expiration_date(self):
        return f"Строк придатності до {self.expiration_date.strftime('%d.%m.%Y')}"
    
    def __str__(self):
        return f"Товар '{self.name_prod}' коштує '{self.price}'."