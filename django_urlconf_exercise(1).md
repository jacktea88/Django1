# Django URLconf 教學練習習題

## 練習主題：線上書店管理系統

### 情境說明
你正在開發一個線上書店管理系統，需要設計完整的URL結構來處理不同的功能頁面。這個練習將幫助你掌握Django URLconf的各種用法和最佳實踐。

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
- [ ] 巢狀資源處理

---

## 第四部分：進階功能實作

### 題目4：複雜URL模式和中間件

**任務：** 實現進階URL功能

**需要實現的功能：**
- 多語言支援
- 子網域路由
- URL重定向規則
- 自訂URL轉換器
- 條件性路由

**要求：**
1. 實現國際化URL
2. 建立自訂路徑轉換器
3. 設定URL重定向規則
4. 處理legacy URL
5. 實現條件性路由邏輯

**預期功能：**
```
/en/books/              -> 英文版書籍列表
/zh/books/              -> 中文版書籍列表
/books/isbn/978-xxx/    -> 使用ISBN查詢書籍
/old/books/1/           -> 重定向到新URL
admin.bookstore.com     -> 管理後台子網域
```

**完成標準：**
- [ ] 多語言URL實現
- [ ] 自訂轉換器功能
- [ ] 重定向規則設定
- [ ] 子網域路由配置

---

## 第五部分：測試和除錯

### 題目5：URL測試和效能優化

**任務：** 建立完整的URL測試案例

**需要完成的測試：**
- URL解析測試
- 反向解析測試
- 參數驗證測試
- 效能基準測試

**要求：**
1. 使用Django TestCase
2. 測試所有URL路徑
3. 驗證參數處理
4. 檢查效能表現
5. 建立測試資料夾結構

**完成標準：**
- [ ] 完整測試覆蓋率
- [ ] 參數邊界測試
- [ ] 效能基準建立
- [ ] 錯誤處理測試

---

## 實作檔案結構

```
bookstore/
├── bookstore/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py          # 主要URL配置
│   └── wsgi.py
├── books/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py          # Books app URL配置
│   └── tests/
│       ├── __init__.py
│       ├── test_urls.py # URL測試
│       └── test_views.py
├── api/
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py          # API URL配置
│   └── serializers.py
└── manage.py
```

---

## 學習重點總結

完成這些練習後，你應該掌握：

### 基礎概念
- URL模式語法
- 路徑參數使用
- include()函數應用
- 命名空間管理

### 進階技巧
- RESTful URL設計
- 自訂路徑轉換器
- 國際化URL處理
- 條件性路由

### 最佳實踐
- URL命名規範
- 錯誤處理策略
- 效能優化技巧
- 測試驅動開發

### 除錯技能
- URL除錯工具使用
- 常見錯誤排除
- 日誌分析方法
- 效能監控

---

## 評分標準

| 項目 | 優秀 (90-100) | 良好 (80-89) | 及格 (70-79) | 不及格 (<70) |
|------|---------------|--------------|--------------|---------------|
| URL配置正確性 | 完全正確 | 小錯誤1-2個 | 錯誤3-5個 | 錯誤很多 |
| 程式碼組織 | 結構清晰 | 組織良好 | 基本整齊 | 結構混亂 |
| 命名規範 | 命名一致 | 大部分一致 | 部分一致 | 命名混亂 |
| 錯誤處理 | 完整處理 | 基本處理 | 部分處理 | 缺乏處理 |
| 測試覆蓋率 | >90% | 70-89% | 50-69% | <50% |
| RESTful設計 | 完全符合 | 大部分符合 | 部分符合 | 不符合 |

---

## 延伸挑戰

完成基礎練習後，可以嘗試：

1. **微服務架構**：設計跨服務的URL路由
2. **GraphQL整合**：實現GraphQL端點
3. **WebSocket支援**：加入即時功能URL
4. **快取策略**：實現URL層級快取
5. **監控整合**：加入URL效能監控

---

## 參考資源

- [Django URL dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/)
- [URL namespaces](https://docs.djangoproject.com/en/stable/topics/http/urls/#url-namespaces)
- [URL reversing](https://docs.djangoproject.com/en/stable/topics/http/urls/#reverse-resolution-of-urls)
- [Path converters](https://docs.djangoproject.com/en/stable/topics/http/urls/#path-converters)

祝你學習愉快！有任何問題都可以提出討論。