"""
URL configuration for bstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mysite.views import homepage, book_list, book_detail, books_by_category, books_by_author

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('books/', book_list, name='book_list'),
    path('detail/<int:book_id>/', book_detail, name='detail'),
    # 書籍分類頁面 - 使用str轉換器
    path('category/<str:category_name>/', books_by_category, name='category'),
    # 作者頁面 - 使用slug轉換器
    path('author/<slug:author_slug>/', books_by_author, name='author'),
    # API端點 - 直接包含，不使用版本控制
    # path('api/', include('api.urls')),
    path('api/', include('api.urls_p')),    
]
