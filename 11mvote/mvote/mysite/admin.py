from django.contrib import admin
from mysite import models

class PollAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'enabled')
    ordering = ('-created_at',)

class PollItemAdmin(admin.ModelAdmin):
    list_display = ('poll', 'name', 'vote', 'image_url')
    ordering = ('poll',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'sku', 'name', 'stock', 'price')
    ordering = ('category',)

admin.site.register(models.Poll, PollAdmin)
admin.site.register(models.PollItem, PollItemAdmin)
admin.site.register(models.VoteCheck)

#產品及分類
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category)
#訂單
admin.site.register(models.Order)
admin.site.register(models.OrderItem)