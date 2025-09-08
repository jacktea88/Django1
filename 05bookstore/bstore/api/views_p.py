from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

# ===== 模擬資料 =====
BOOKS_DATA = [
    {'id': 1, 'title': 'Python程式設計', 'author': '王小明', 'price': 450, 'category_id': 1},
    {'id': 2, 'title': 'Django網頁開發', 'author': '李小華', 'price': 520, 'category_id': 1},
    {'id': 3, 'title': '資料結構與演算法', 'author': '張大同', 'price': 380, 'category_id': 2},
    {'id': 4, 'title': '機器學習入門', 'author': '陳小美', 'price': 600, 'category_id': 3},
]

CATEGORIES_DATA = [
    {'id': 1, 'name': 'Programming', 'description': '程式設計相關書籍'},
    {'id': 2, 'name': 'Computer Science', 'description': '計算機科學相關書籍'},
    {'id': 3, 'name': 'Machine Learning', 'description': '機器學習相關書籍'},
]

REVIEWS_DATA = [
    {'id': 1, 'book_id': 1, 'rating': 5, 'comment': '很棒的書！', 'user': '讀者A'},
    {'id': 2, 'book_id': 1, 'rating': 4, 'comment': '內容豐富', 'user': '讀者B'},
    {'id': 3, 'book_id': 2, 'rating': 5, 'comment': 'Django入門首選', 'user': '讀者C'},
]

# ===== 輔助函數 =====
def fine_book_by_id(book_id):
    """根據ID尋找書籍"""
    print(f"尋找ID為{book_id}的書籍...")
    for book in BOOKS_DATA:
        if book['id'] == book_id:
            return book
    return None

def get_reviews_by_book_id(book_id):
    """根據書籍ID獲取評論列表"""
    print(f"獲取ID為{book_id}的書籍評論...")
    for review in REVIEWS_DATA:
        if review['book_id'] == book_id:
            return review
    return None

def find_category_by_id(category_id):
    """根據ID尋找書籍類別"""
    print(f"尋找ID為{category_id}的書籍類別...")
    for category in CATEGORIES_DATA:
        if category['id'] == category_id:
            return category
    return None

def get_next_id(data_list):
    """獲取下一個ID"""
    if not data_list:
        return 1
    return max([item['id'] for item in data_list]) + 1

def api_home(request):
    """API首頁"""

    return JsonResponse({
        'message': 'Welcome to Bookstore API',
        'version': '1.0',
        'endpoints': {
            'books': '/api/books/?category=category_id&search=keyword',
            'book': '/api/books/{book_id}/',
            'categories': '/api/categories/',
            'category': '/api/categories/{category_id}/',
            'reviews': '/api/books/{book_id}/reviews/',
            'review': '/api/books/{book_id}/reviews/{review_id}/',
        }
        })

@csrf_exempt
def books_list(request):
    """書籍列表端點
    # get
    # http://127.0.0.1:8000/api/books/?category=1
    # http://127.0.0.1:8000/api/books/?search=王小明

    # post
    # http://localhost:8000/api/books/
    {"id": 1, "title": "Python\u7a0b\u5f0f\u8a2d\u8a08", "author": "\u738b\u5c0f\u660e", "price": 900, "category_id": 1}
    """
    books = BOOKS_DATA.copy()
    if request.method == 'GET':
        category = request.GET.get('category')
        search = request.GET.get('search')

        if category:
            try:
                category_id = int(category)
                books = [book for book in BOOKS_DATA if book['category_id'] == category_id]
            except ValueError:
                return JsonResponse({'error': 'Invalid category ID'}, status=400)

        if search:
            books = [book for book in BOOKS_DATA 
                    if search.lower() in book['title'].lower() or 
                    search.lower() in book['author'].lower()]

        return JsonResponse({
            'count': len(books),
            'books': books
            })
    elif request.method == 'POST':
        
        try:
            data = json.loads(request.body)
            book = {
                'id': len(books) + 1,
                'title': data['title'],
                'author': data['author'],
                'price': data['price'],
                'category_id': data['category_id']
            }
            BOOKS_DATA.append(book)
            return JsonResponse({
                'status': 'success', 
                'message': 'Book added successfully',
                'book': book})  #注意，列出新加入的書籍就好
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

        # return JsonResponse({'books': BOOKS_DATA})
    
@csrf_exempt
def book_detail(request, book_id):
    """單本書籍詳細資訊端點
    GET:
    http://localhost:8000/api/books/1/
    PUT:
    http://localhost:8000/api/books/1/ 
    json:
    {"id": 6, "title": "Python\u7a0b\u5f0f\u8a2d\u8a08", "author": "\u738b\u5c0f\u660e", "price": 1000, "category_id": 1}
    DELETE:
    http://localhost:8000/api/books/1/
    
    """
    book = fine_book_by_id(book_id)
    if not book:
        return JsonResponse({'error': 'Book not found'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({'book': book})
    
    elif request.method == 'PUT': #注意測試時!!!!!網址id要正確，網址最後要有斜線!!!!!
        try:
            data = json.loads(request.body)
            
            # 更新書籍資料
            book.update(data)
            
            return JsonResponse({
                'message': 'Book updated successfully',
                'book': book
            })
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        
    elif request.method == 'DELETE':
        # 刪除書籍資料
        BOOKS_DATA.remove(book)
        return JsonResponse({
            'message': 'Book deleted successfully',
            'book': book
        })
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
@csrf_exempt
def book_reviews(request, book_id):
    """書籍評論端點
    GET:
    http://localhost:8000/api/books/1/reviews/
    POST:
    http://localhost:8000/api/books/1/reviews/
    json:
    {
        "id": 3,
        "book_id": 2,
        "rating": 5,
        "comment": "Django入門首選",
        "user": "讀者C"
    }

    """

    # 檢查書籍是否存在
    book = fine_book_by_id(book_id)
    if not book:
        return JsonResponse({'error': 'Book not found'}, status=404)
    
    if request.method == 'GET':
        reviews = get_reviews_by_book_id(book_id)
        print(f'獲取ID為{book_id}的書籍評論...{reviews}',reviews)
        return JsonResponse({
            'book_title': book['title'],
            'reviews': reviews
        })
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            new_review = {
                'id': get_next_id(REVIEWS_DATA),
                'book_id': book_id,
                'rating': data.get('rating', 5),
                'comment': data.get('comment', ''),
                'user': data.get('user', 'Anonymous')
            }
            
            REVIEWS_DATA.append(new_review)
            return JsonResponse({
                'message': 'Review added successfully',
                'review': new_review
            })
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
def categories_list(request):
    """分類列表端點
    http://localhost:8000/api/categories/
    """
    return JsonResponse({'categories': CATEGORIES_DATA})

def category_detail(request, category_id):
    """特定分類書籍端點
    http://localhost:8000/api/categories/1/
    """
    category = find_category_by_id(category_id)
    if not category:
        return JsonResponse({'error': 'Category not found'}, status=404)
    
    # 取得該分類的書籍
    books = [book for book in BOOKS_DATA if book['category_id'] == category_id]
    
    return JsonResponse({
        'category': category,
        'books_count': len(books),
        'books': books
    })