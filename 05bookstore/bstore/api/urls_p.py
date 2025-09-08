from django.urls import path
from . import views_p

urlpatterns = [
    path('', views_p.api_home, name='api_home'),
    # ===== 書籍相關 =====
    # GET /api/books/ - 取得書籍列表
    # POST /api/books/ - 新增書籍
    path('books/', views_p.books_list, name='books_list'),
]