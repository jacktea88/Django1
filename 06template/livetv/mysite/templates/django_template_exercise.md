# Django Template 練習題 - Base.html & Header.html 架構

## 練習目標
學習使用Django template的繼承機制，建立可重複使用的網頁架構，包含base.html和header.html的設計與運用。

## 練習要求

### 第一部分：建立基礎架構

#### 1. 建立 `base.html` 模板
- 包含完整的HTML5文檔結構
- 定義以下區塊(blocks)：
  - `title` - 頁面標題
  - `extra_css` - 額外CSS樣式
  - `header` - 頁面標頭區域
  - `content` - 主要內容區域
  - `footer` - 頁腳區域
  - `extra_js` - 額外JavaScript

#### 2. 建立 `header.html` 模板
- 包含網站Logo
- 導航選單（首頁、關於我們、服務項目、聯絡我們）
- 使用者登入狀態顯示
- RWD響應式設計

### 第二部分：建立子頁面模板

#### 3. 建立 `home.html` 首頁模板
- 繼承base.html
- 包含歡迎訊息
- 顯示最新消息列表（使用迴圈）
- 包含輪播圖區域

#### 4. 建立 `about.html` 關於我們頁面
- 繼承base.html  
- 公司介紹內容
- 團隊成員展示（使用迴圈顯示）
- 公司歷史時間軸

#### 5. 建立 `services.html` 服務項目頁面
- 繼承base.html
- 服務項目卡片展示
- 使用template filter格式化價格
- 包含搜尋功能

#### 6. 建立 `contact.html` 聯絡我們頁面
- 繼承base.html
- 聯絡表單
- 公司地址和聯絡資訊
- Google Maps嵌入

### 第三部分：進階功能

#### 7. 建立 `product_list.html` 產品列表頁面
- 繼承base.html
- 產品分頁功能
- 產品篩選和排序
- 產品搜尋結果顯示

#### 8. 建立 `product_detail.html` 產品詳情頁面
- 繼承base.html
- 產品詳細資訊顯示
- 相關產品推薦
- 使用者評論區塊

## 技術要求

### Template 語法運用：
- `{% extends %}` - 模板繼承
- `{% include %}` - 模板包含
- `{% block %}` - 區塊定義
- `{% for %}` - 迴圈結構
- `{% if %}` - 條件判斷
- `{{ variable }}` - 變數顯示
- `{{ variable|filter }}` - 過濾器使用

### CSS Framework：
- 使用Bootstrap 5或Tailwind CSS
- 實作RWD響應式設計
- 自定義CSS樣式

### JavaScript 功能：
- 導航選單互動
- 表單驗證
- 輪播圖功能
- 搜尋即時預覽

## 範例資料結構

### Context 資料：
```python
# views.py 範例資料
context = {
    'site_name': '我的網站',
    'user': request.user,
    'news_list': [
        {'title': '最新消息1', 'date': '2024-01-01', 'content': '...'},
        {'title': '最新消息2', 'date': '2024-01-02', 'content': '...'},
    ],
    'team_members': [
        {'name': '張三', 'position': '執行長', 'photo': 'ceo.jpg'},
        {'name': '李四', 'position': '技術長', 'photo': 'cto.jpg'},
    ],
    'services': [
        {'name': '網頁設計', 'price': 50000, 'description': '...'},
        {'name': 'APP開發', 'price': 100000, 'description': '...'},
    ],
    'products': [
        {'name': '產品A', 'price': 1200, 'category': '3C'},
        {'name': '產品B', 'price': 800, 'category': '服飾'},
    ]
}
```

## 評分標準

1. **架構設計 (25分)**
   - base.html架構完整性
   - header.html重複使用性
   - 區塊設計合理性

2. **Template語法 (25分)**
   - 正確使用繼承和包含
   - 迴圈和條件判斷運用
   - 過濾器使用

3. **頁面功能 (25分)**
   - 所有頁面正常顯示
   - 導航功能正常
   - 資料正確渲染

4. **設計美觀 (15分)**
   - CSS樣式設計
   - RWD響應式效果
   - 使用者體驗

5. **程式碼品質 (10分)**
   - 程式碼整潔度
   - 註解完整性
   - 檔案組織結構

## 提交要求

1. 完整的template檔案
2. 對應的views.py檔案
3. static檔案（CSS, JS, 圖片）
4. README.md說明文件
5. 專案執行截圖

## 額外挑戰

1. 實作多語言支援（i18n）
2. 加入breadcrumb麵包屑導航
3. 實作網站搜尋功能
4. 加入社群媒體分享按鈕
5. 實作無限滾動載入

## 學習重點

- 理解Django template繼承機制
- 掌握template語法和過濾器
- 學習模塊化網頁設計思維
- 實踐前端與後端整合
- 培養良好的程式碼組織習慣