from django.contrib import admin
from mysite.models import Post

# Register your models here.
# admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date', 'body', )

# 記得拿掉上面的註冊，否則會報錯(重覆註冊)
admin.site.register(Post, PostAdmin)

