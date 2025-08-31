# Django Template 表格練習習題

## 練習題目：學生成績管理系統

### 情境說明
你正在開發一個學生成績管理系統，需要建立一個頁面來顯示學生的成績資料。這個練習將幫助你掌握Django template中表格的使用技巧。

---

## 第一部分：基礎表格顯示

### 題目1：建立基本學生資料表格

**任務：** 建立一個Django template來顯示學生基本資料

**提供的資料結構：**
```python
# views.py
students = [
    {'id': 1, 'name': '張小明', 'age': 20, 'class': 'A班'},
    {'id': 2, 'name': '李小華', 'age': 19, 'class': 'B班'},
    {'id': 3, 'name': '王小美', 'age': 21, 'class': 'A班'},
    {'id': 4, 'name': '陳小強', 'age': 20, 'class': 'C班'},
]
```

**要求：**
1. 使用HTML表格標籤 `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>`
2. 表格需要包含欄位：學號、姓名、年齡、班級
3. 為表格添加基本的CSS樣式
4. 使用Django的for迴圈來遍歷學生資料

---

## 第二部分：進階表格功能

### 題目2：成績表格with條件格式

**任務：** 擴展表格功能，加入成績顯示和條件格式

**提供的資料結構：**
```python
# views.py
student_grades = [
    {'id': 1, 'name': '張小明', 'chinese': 85, 'math': 92, 'english': 78},
    {'id': 2, 'name': '李小華', 'chinese': 90, 'math': 76, 'english': 88},
    {'id': 3, 'name': '王小美', 'chinese': 72, 'english': 85, 'math': 90},
    {'id': 4, 'name': '陳小強', 'chinese': 88, 'math': 95, 'english': 82},
]
```

**要求：**
1. 顯示學生姓名、國文、數學、英文成績
2. 計算並顯示平均分數
3. 使用條件判斷：
   - 平均分數 ≥ 85：顯示綠色背景
   - 平均分數 70-84：顯示黃色背景  
   - 平均分數 < 70：顯示紅色背景
4. 加入表格排序功能提示

---

## 第三部分：複合表格應用

### 題目3：響應式成績統計表格

**任務：** 建立一個響應式的成績統計表格

**提供的資料結構：**
```python
# views.py
class_summary = [
    {
        'class_name': 'A班',
        'total_students': 25,
        'subjects': {
            'chinese': {'avg': 82.5, 'highest': 95, 'lowest': 65},
            'math': {'avg': 78.2, 'highest': 98, 'lowest': 45},
            'english': {'avg': 85.1, 'highest': 96, 'lowest': 72}
        }
    },
    {
        'class_name': 'B班', 
        'total_students': 23,
        'subjects': {
            'chinese': {'avg': 79.8, 'highest': 92, 'lowest': 58},
            'math': {'avg': 84.3, 'highest': 100, 'lowest': 62},
            'english': {'avg': 81.7, 'highest': 94, 'lowest': 69}
        }
    }
]
```

**要求：**
1. 建立巢狀表格結構
2. 使用colspan和rowspan合併儲存格
3. 實作響應式設計（手機版顯示調整）
4. 加入表格標題和說明
5. 使用Django template的巢狀迴圈

---


