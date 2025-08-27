# Django URLconf 練習習題

## 練習主題：線上書店管理系統

### 情境說明
你正在開發一個線上書店管理系統，需要設計完整的URL結構來處理不同的功能頁面。這個練習可運用Django URLconf的各種用法。

#### ===== 模擬資料 =====
##### 習題一 模擬書籍資料
    books = [
        {'id': 1, 'title': 'Python程式設計', 'author': '王小明', 'price': 450},
        {'id': 2, 'title': 'Django網頁開發', 'author': '李小華', 'price': 520},
        {'id': 3, 'title': '資料結構與演算法', 'author': '張大同', 'price': 380},
    ]
    
    context = {
        'books': books,
        'page_title': '書籍列表'
    }

##### 習題二 模擬書籍資料
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

##### 習題三 模擬書籍資料
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

---

## 第一部分：基礎URL配置

### 題目1：建立基本URL結構

**任務：** 為書店系統建立基本的URL配置

**需要實現的頁面：**
- 首頁：顯示書店介紹
- 書籍列表：顯示所有書籍
- 關於我們：公司介紹頁面
- 聯絡我們：聯絡資訊頁面

**要求：**
1. 建立主專案的 `urls.py` 
2. 建立 books app 的 `urls.py`
3. 使用 `include()` 函數組織URL
4. 設定適當的URL命名 (name參數)
5. 建立對應的view函數

**預期URL結構：**
```
/                    -> 首頁
/books/              -> 書籍列表
/about/              -> 關於我們  
/contact/            -> 聯絡我們
```

**完成標準：**
- [ ] URL路由正確配置
- [ ] 使用include()組織結構
- [ ] 每個URL都有適當的名稱
- [ ] View函數能正常回應

---

## 第二部分：帶參數的URL

### 題目2：動態URL參數處理

**任務：** 實現書籍詳細頁面和分類功能

**需要實現的功能：**
- 書籍詳細頁面：顯示單本書的詳細資訊
- 書籍分類頁面：依據分類顯示書籍
- 作者頁面：顯示特定作者的所有書籍
- 搜尋功能：根據關鍵字搜尋書籍

**要求：**
1. 使用路徑參數 (`<int:pk>`, `<str:slug>`)
2. 實現URL反向解析
3. 處理可選參數
4. 加入查詢字串參數處理
5. 設定URL參數驗證

**預期URL結構：**
```
/books/1/                    -> 書籍詳細頁面 (ID=1)
/books/category/fiction/     -> 小說分類頁面
/books/author/john-doe/      -> 作者頁面
/books/search/               -> 搜尋頁面
/books/search/?q=python      -> 搜尋結果頁面
```

**完成標準：**
- [ ] 正確使用路徑參數
- [ ] URL反向解析功能
- [ ] 參數驗證和錯誤處理
- [ ] 查詢字串參數處理

---

## 第三部分：進階URL配置

### 題目3：RESTful API風格URL

**任務：** 設計RESTful風格的API端點

**需要實現的API端點：**
- 書籍CRUD操作
- 評論系統
- 購物車功能
- 訂單管理

**要求：**
1. 遵循RESTful設計原則
2. 使用HTTP方法區分操作
3. 實現版本控制
4. 加入API認證考量
5. 建立API文件結構

**預期API結構：**
```
GET    /api/v1/books/              -> 取得書籍列表
POST   /api/v1/books/              -> 新增書籍
GET    /api/v1/books/1/            -> 取得特定書籍
PUT    /api/v1/books/1/            -> 更新書籍
DELETE /api/v1/books/1/            -> 刪除書籍
GET    /api/v1/books/1/reviews/    -> 書籍評論列表
POST   /api/v1/books/1/reviews/    -> 新增評論
```

**完成標準：**
- [ ] RESTful URL設計
- [ ] HTTP方法正確對應
- [ ] API版本控制


---







## 參考資源

- [Django URL dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/)
- [URL namespaces](https://docs.djangoproject.com/en/stable/topics/http/urls/#url-namespaces)
- [URL reversing](https://docs.djangoproject.com/en/stable/topics/http/urls/#reverse-resolution-of-urls)
- [Path converters](https://docs.djangoproject.com/en/stable/topics/http/urls/#path-converters)

