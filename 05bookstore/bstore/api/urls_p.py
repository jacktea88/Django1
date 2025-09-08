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
    
    # ===== 書籍評論端點 =====
    # GET /api/books/1/reviews/ - 取得書籍評論
    # POST /api/books/1/reviews/ - 新增評論
    path('books/<int:book_id>/reviews/', views_p.book_reviews, name='book_reviews'),
    
    # GET /api/books/1/reviews/1/ - 取得特定評論
    # PUT /api/books/1/reviews/1/ - 更新評論
    # DELETE /api/books/1/reviews/1/ - 刪除評論
    # path('books/<int:book_id>/reviews/<int:review_id>/', views_p.review_detail, name='review_detail'),
    
    # ===== 分類端點 =====
    # GET /api/categories/ - 取得所有分類
    path('categories/', views_p.categories_list, name='categories_list'),
    
    # GET /api/categories/1/ - 取得特定分類
    path('categories/<int:category_id>/', views_p.category_detail, name='category_detail'),
]