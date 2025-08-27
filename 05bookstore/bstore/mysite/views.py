from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404

MOCK_BOOKS = [
    {
        'id': 1, 'title': 'Python程式設計', 'author': '王小明', 
        'author_slug': 'wang-xiaoming', 'category': 'programming', 
        'price': 450, 'isbn': '978-1-234-56789-0', 'year': 2023
    },
    {
        'id': 2, 'title': 'Django網頁開發', 'author': '李小華', 
        'author_slug': 'li-xiaohua', 'category': 'web-development', 
        'price': 520, 'isbn': '978-1-234-56789-1', 'year': 2024
    },
    {
        'id': 3, 'title': '資料結構與演算法', 'author': '張大同', 
        'author_slug': 'zhang-datong', 'category': 'computer-science', 
        'price': 380, 'isbn': '978-1-234-56789-2', 'year': 2023
    },
    {
        'id': 4, 'title': '機器學習實戰', 'author': '王小明', 
        'author_slug': 'wang-xiaoming', 'category': 'machine-learning', 
        'price': 600, 'isbn': '978-1-234-56789-3', 'year': 2024
    },
]


# Create your views here.
def book_list(request):
    # 模擬書籍資料
    books = [
        {'id': 1, 'title': 'Python程式設計', 'author': '王小明', 'price': 450},
        {'id': 2, 'title': 'Django網頁開發', 'author': '李小華', 'price': 520},
        {'id': 3, 'title': '資料結構與演算法', 'author': '張大同', 'price': 380},
    ]
    
    context = {
        'books': books,
        'mock_books': MOCK_BOOKS,
        'page_title': '書籍列表'
    }
    # return JsonResponse(context, status=200)
    return render(request, 'book_list.html', locals())

def homepage(request):
    return render(request, 'index.html', locals())

def book_detail(request, book_id):
    """書籍詳細頁面 - 使用book_id參數"""
    try:
        book = next(book for book in MOCK_BOOKS if book['id'] == book_id)
        print(book)
    except StopIteration:
        raise Http404("書籍不存在")
    
    context = {
        'book': book,
        'page_title': f'書籍詳情 - {book["title"]}'
    }
    return render(request, 'book_detail.html', context)

def books_by_category(request, category_name):
    """依分類顯示書籍"""
    filtered_books = []
    for book in MOCK_BOOKS:
        if book['category'] == category_name:
            filtered_books.append(book)
    
    if not filtered_books:
        raise Http404(f"分類 '{category_name}' 不存在或無書籍")
    
    context = {
        'books': filtered_books,
        'category_name': category_name,
        'page_title': f'分類：{category_name}'
    }
    return render(request, 'category.html', context)

def books_by_author(request, author_slug):
    """依作者顯示書籍"""
    filtered_books = [
        book for book in MOCK_BOOKS 
        if book['author_slug'] == author_slug
    ]
    
    if not filtered_books:
        raise Http404(f"作者 '{author_slug}' 不存在或無書籍")
    
    context = {
        'books': filtered_books,
        'author_name': filtered_books[0]['author'],
        'page_title': f'作者：{filtered_books[0]["author"]}'
    }
    return render(request, 'author.html', context)

#/search/?q=keyword
def book_search(request):
    """書籍搜尋功能"""
    query = request.GET.get('q', '')
    books = []
    
    if query:
        # 搜尋書名或作者
        books = [
            book for book in MOCK_BOOKS 
            if query.lower() in book['title'].lower() or 
               query.lower() in book['author'].lower()
        ]
    
    context = {
        'books': books,
        'query': query,
        'page_title': f'搜尋結果: {query}' if query else '書籍搜尋'
    }
    return render(request, 'search.html', context)

def book_by_isbn(request, isbn):
    """使用ISBN查詢書籍"""
    try:
        book = next(book for book in MOCK_BOOKS if book['isbn'] == isbn)
    except StopIteration:
        raise Http404(f"ISBN '{isbn}' 的書籍不存在")
    
    context = {
        'book': book,
        'page_title': f'ISBN: {isbn}'
    }
    return render(request, 'book_detail.html', context)

def books_by_year(request, year):
    """依出版年份顯示書籍"""
    filtered_books = [
        book for book in MOCK_BOOKS 
        if book['year'] == year
    ]
    
    context = {
        'books': filtered_books,
        'year': year,
        'page_title': f'{year}年出版書籍'
    }
    return render(request, 'year.html', context)

def book_list_paginated(request, page=1):
    """分頁書籍列表"""
    paginator = Paginator(MOCK_BOOKS, 2)  # 每頁2本書
    
    try:
        books_page = paginator.page(page)
    except:
        raise Http404("頁面不存在")
    
    context = {
        'books_page': books_page,
        'page_title': f'書籍列表 - 第{page}頁'
    }
    return render(request, 'book_list_paginated.html', context)