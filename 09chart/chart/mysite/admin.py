from django.contrib import admin
from mysite.models import Vote, User

# Register your models here.
admin.site.register(User)
admin.site.register(Vote)