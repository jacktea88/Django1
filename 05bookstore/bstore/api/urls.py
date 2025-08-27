"""
API URL配置 - 簡化版RESTful設計
"""
from django.urls import path
from . import views

urlpatterns = [
    # API首頁
    path('', views.api_home, name='api_home'),
    
    # ===== 書籍相關端點 =====
    # GET /api/books/ - 取得書籍列表
    # POST /api/books/ - 新增書籍
    path('books/', views.books_list, name='books_list'),
    
    # GET /api/books/1/ - 取得特定書籍
    # PUT /api/books/1/ - 更新書籍  
    # DELETE /api/books/1/ - 刪除書籍
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    
    # ===== 書籍評論端點 =====
    # GET /api/books/1/reviews/ - 取得書籍評論
    # POST /api/books/1/reviews/ - 新增評論
    path('books/<int:book_id>/reviews/', views.book_reviews, name='book_reviews'),
    
    # GET /api/books/1/reviews/1/ - 取得特定評論
    # PUT /api/books/1/reviews/1/ - 更新評論
    # DELETE /api/books/1/reviews/1/ - 刪除評論
    path('books/<int:book_id>/reviews/<int:review_id>/', views.review_detail, name='review_detail'),
    
    # ===== 分類端點 =====
    # GET /api/categories/ - 取得所有分類
    path('categories/', views.categories_list, name='categories_list'),
    
    # GET /api/categories/1/ - 取得特定分類
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    
    # ===== 作者端點 =====
    # GET /api/authors/ - 取得所有作者
    path('authors/', views.authors_list, name='authors_list'),
    
    # GET /api/authors/1/ - 取得特定作者
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    
    # GET /api/authors/1/books/ - 取得作者的書籍
    path('authors/<int:author_id>/books/', views.author_books, name='author_books'),
    
    # ===== 購物車端點 =====
    # GET /api/cart/ - 取得購物車
    # POST /api/cart/ - 更新購物車
    path('cart/', views.cart, name='cart'),
    
    # ===== 訂單端點 =====  
    # GET /api/orders/ - 取得訂單列表
    # POST /api/orders/ - 建立訂單
    path('orders/', views.orders_list, name='orders_list'),
    
    # GET /api/orders/1/ - 取得特定訂單
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    
    # ===== 搜尋端點 =====
    # GET /api/search/?q=keyword - 搜尋功能
    path('search/', views.search, name='search'),
]