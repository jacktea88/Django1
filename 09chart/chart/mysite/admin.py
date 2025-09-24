from django.contrib import admin
from mysite.models import Vote, User, Profile

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Vote)