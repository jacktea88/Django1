from django.urls import path
from . import views_p

urlpatterns = [
    path('', views_p.api_home, name='api_home'),
    # ===== 書籍相關 =====
    # GET /api/books/ - 取得書籍列表
    # POST /api/books/ - 新增書籍
    path('books/', views_p.books_list, name='books_list'),
    
    # GET /api/books/1/ - 取得特定書籍
    # PUT /api/books/1/ - 更新書籍  
    # DELETE /api/books/1/ - 刪除書籍
    path('books/<int:book_id>/', views_p.book_detail, name='book_detail'),
]