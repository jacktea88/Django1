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
    for book in BOOKS_DATA:
        if book['id'] == book_id:
            return book
    return None

def api_home(request):
    """API首頁"""

    return JsonResponse({
        'message': 'Welcome to Bookstore API',
        'version': '1.0',
        'endpoints': {
            'books': '/api/books/?category=category_id&search=keyword',
        }
        })


def books_list(request):
    """書籍列表頁面"""
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

        return JsonResponse({'books': BOOKS_DATA})
    