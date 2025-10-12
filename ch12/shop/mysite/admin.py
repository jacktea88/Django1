from django.contrib import admin
from mysite import models


# product list display
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'stock', 'price', 'sku')
    ordering = ['category']

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Profile)
admin.site.register(models.Vote)

# register for product, category
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category)

# for order
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
