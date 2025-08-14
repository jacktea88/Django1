from django.contrib import admin
from mysite.models import Post, Product, NewTable

# Register your models here.
# admin.site.register(Post)

admin.site.register(Product)
admin.site.register(NewTable)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date', 'body', )

# 記得拿掉上面的註冊，否則會報錯(重覆註冊)
admin.site.register(Post, PostAdmin)

