from django.contrib import admin
from mysite.models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'price', 'stock')
    ordering = ('category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)