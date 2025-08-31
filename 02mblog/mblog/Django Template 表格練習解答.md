# Django Template 表格練習解答 (題目1-3)

## 題目1 解答：基本學生資料表格

### urls.py
```python
from django.urls import path
from mysite.views import student_list

urlpatterns = [
    path('students/', student_list, name='student_list'), 
]

```
### views.py
```python
from django.shortcuts import render

def student_list(request):
    students = [
        {'id': 1, 'name': '張小明', 'age': 20, 'class': 'A班'},
        {'id': 2, 'name': '李小華', 'age': 19, 'class': 'B班'},
        {'id': 3, 'name': '王小美', 'age': 21, 'class': 'A班'},
        {'id': 4, 'name': '陳小強', 'age': 20, 'class': 'C班'},
    ]
    return render(request, 'student_list.html', {'students': students})
```

### templates/students/student_list.html
```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>學生資料列表</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }
        
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        
        .student-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        
        .student-table th,
        .student-table td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        
        .student-table th {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            text-align: center;
        }
        
        .student-table tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        
        .student-table tr:hover {
            background-color: #e8f5e8;
        }
        
        .student-table td {
            text-align: center;
        }
        
        .no-data {
            text-align: center;
            color: #666;
            font-style: italic;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>學生資料管理系統</h1>
        
        {% if students %}
            <table class="student-table">
                <thead>
                    <tr>
                        <th>學號</th>
                        <th>姓名</th>
                        <th>年齡</th>
                        <th>班級</th>
                    </tr>
                </thead>
                <tbody>
                    {% for student in students %}
                        <tr>
                            <td>{{ student.id }}</td>
                            <td>{{ student.name }}</td>
                            <td>{{ student.age }}</td>
                            <td>{{ student.class }}</td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        {% else %}
            <div class="no-data">
                目前沒有學生資料
            </div>
        {% endif %}
    </div>
</body>
</html>
```

---

## 題目2 解答：成績表格with條件格式

### urls.py
```python
from django.urls import path
from mysite.views import student_grades

urlpatterns = [
    path('grades/', student_grades, name='student_grades'),
]

```
### views.py
```python
from django.shortcuts import render

def student_grades(request):
    student_grades = [
        {'id': 1, 'name': '張小明', 'chinese': 85, 'math': 92, 'english': 78},
        {'id': 2, 'name': '李小華', 'chinese': 90, 'math': 76, 'english': 88},
        {'id': 3, 'name': '王小美', 'chinese': 72, 'english': 85, 'math': 90},
        {'id': 4, 'name': '陳小強', 'chinese': 88, 'math': 95, 'english': 82},
    ]
    
    # 計算平均分數 (在template中也可以使用custom filter)
    for student in student_grades:
        total = student['chinese'] + student['math'] + student['english']
        student['average'] = round(total / 3, 1)
    
    return render(request, 'student_grades.html', {'student_grades': student_grades})
```

### templates/students/student_grades.html
```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>學生成績管理</title>
    <style>
        body {
            font-family: 'Microsoft JhengHei', Arial, sans-serif;
            margin: 20px;
            background-color: #f8f9fa;
        }
        
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            max-width: 1000px;
            margin: 0 auto;
        }
        
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2em;
        }
        
        .grades-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            font-size: 14px;
        }
        
        .grades-table th,
        .grades-table td {
            border: 1px solid #dee2e6;
            padding: 15px;
            text-align: center;
        }
        
        .grades-table th {
            background-color: #343a40;
            color: white;
            font-weight: bold;
            position: sticky;
            top: 0;
        }
        
        .grades-table tr:nth-child(even) {
            background-color: #f8f9fa;
        }
        
        .grades-table tr:hover {
            background-color: #e9ecef;
            transform: translateY(-1px);
            transition: all 0.2s ease;
        }
        
        /* 條件格式樣式 */
        .grade-excellent {
            background-color: #d4edda !important;
            color: #155724;
            font-weight: bold;
        }
        
        .grade-good {
            background-color: #fff3cd !important;
            color: #856404;
        }
        
        .grade-poor {
            background-color: #f8d7da !important;
            color: #721c24;
        }
        
        .student-name {
            font-weight: bold;
            text-align: left;
        }
        
        .average-score {
            font-weight: bold;
            font-size: 1.1em;
        }
        
        .legend {
            display: flex;
            justify-content: center;
            margin-top: 20px;
            gap: 20px;
        }
        
        .legend-item {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        
        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 3px;
        }
        
        .stats {
            background-color: #e9ecef;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 學生成績管理系統</h1>
        
        {% if student_grades %}
            <div class="stats">
                <strong>班級總人數：{{ student_grades|length }} 人</strong>
            </div>
            
            <table class="grades-table">
                <thead>
                    <tr>
                        <th>學號</th>
                        <th>姓名</th>
                        <th>國文</th>
                        <th>數學</th>
                        <th>英文</th>
                        <th>平均分數</th>
                        <th>等級</th>
                    </tr>
                </thead>
                <tbody>
                    {% for student in student_grades %}
                        <tr>
                            <td>{{ student.id|stringformat:"03d" }}</td>
                            <td class="student-name">{{ student.name }}</td>
                            <td>{{ student.chinese }}</td>
                            <td>{{ student.math }}</td>
                            <td>{{ student.english }}</td>
                            
                            <!-- 平均分數with條件格式 -->
                            {% if student.average >= 85 %}
                                <td class="average-score grade-excellent">{{ student.average }}</td>
                                <td class="grade-excellent">優秀 🌟</td>
                            {% elif student.average >= 70 %}
                                <td class="average-score grade-good">{{ student.average }}</td>
                                <td class="grade-good">良好 👍</td>
                            {% else %}
                                <td class="average-score grade-poor">{{ student.average }}</td>
                                <td class="grade-poor">待加強 📚</td>
                            {% endif %}
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
            
            <!-- 圖例說明 -->
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-color grade-excellent"></div>
                    <span>優秀 (≥85分)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color grade-good"></div>
                    <span>良好 (70-84分)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color grade-poor"></div>
                    <span>待加強 (<70分)</span>
                </div>
            </div>
            
        {% else %}
            <div class="no-data">
                目前沒有成績資料
            </div>
        {% endif %}
    </div>
</body>
</html>
```

---

## 題目3 解答：響應式成績統計表格

### views.py
```python
from django.shortcuts import render

def class_summary(request):
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
    
    return render(request, 'students/class_summary.html', {'class_summary': class_summary})
```

### templates/students/class_summary.html
```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>班級成績統計</title>
    <style>
        * {
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Microsoft JhengHei', Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f1f3f4;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.2em;
        }
        
        .summary-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 14px;
            overflow-x: auto;
        }
        
        .summary-table th,
        .summary-table td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: center;
        }
        
        .summary-table th {
            background-color: #34495e;
            color: white;
            font-weight: bold;
            position: sticky;
            top: 0;
            z-index: 10;
        }
        
        .summary-table .class-header {
            background-color: #3498db;
            color: white;
            font-weight: bold;
            font-size: 1.1em;
        }
        
        .summary-table .subject-header {
            background-color: #95a5a6;
            color: white;
            writing-mode: vertical-rl;
            text-orientation: mixed;
            padding: 8px 4px;
            min-width: 40px;
        }
        
        .summary-table .stat-cell {
            font-weight: bold;
        }
        
        .avg-cell { background-color: #e8f8f5; }
        .highest-cell { background-color: #d5f4e6; }
        .lowest-cell { background-color: #fadbd8; }
        
        .total-students {
            background-color: #f8f9fa;
            font-weight: bold;
        }
        
        /* 響應式設計 */
        .table-wrapper {
            overflow-x: auto;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        @media screen and (max-width: 768px) {
            body {
                padding: 10px;
            }
            
            .container {
                padding: 15px;
            }
            
            h1 {
                font-size: 1.8em;
            }
            
            .summary-table {
                font-size: 12px;
            }
            
            .summary-table th,
            .summary-table td {
                padding: 8px 4px;
            }
            
            .subject-header {
                writing-mode: horizontal-tb !important;
                text-orientation: mixed;
                padding: 4px !important;
                min-width: auto !important;
            }
        }
        
        @media screen and (max-width: 480px) {
            .summary-table {
                font-size: 10px;
            }
            
            .summary-table th,
            .summary-table td {
                padding: 6px 2px;
            }
            
            h1 {
                font-size: 1.5em;
            }
        }
        
        .legend {
            margin-top: 20px;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 8px;
        }
        
        .legend h3 {
            margin-top: 0;
            color: #2c3e50;
        }
        
        .legend-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 10px;
            margin-top: 10px;
        }
        
        .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 3px;
            border: 1px solid #ccc;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📈 班級成績統計報表</h1>
        
        {% if class_summary %}
            <div class="table-wrapper">
                <table class="summary-table">
                    <thead>
                        <tr>
                            <th rowspan="2">班級</th>
                            <th rowspan="2">總人數</th>
                            <th colspan="3">國文</th>
                            <th colspan="3">數學</th>
                            <th colspan="3">英文</th>
                        </tr>
                        <tr>
                            <th class="subject-header">平均</th>
                            <th class="subject-header">最高</th>
                            <th class="subject-header">最低</th>
                            <th class="subject-header">平均</th>
                            <th class="subject-header">最高</th>
                            <th class="subject-header">最低</th>
                            <th class="subject-header">平均</th>
                            <th class="subject-header">最高</th>
                            <th class="subject-header">最低</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for class_data in class_summary %}
                            <tr>
                                <td class="class-header">{{ class_data.class_name }}</td>
                                <td class="total-students">{{ class_data.total_students }}</td>
                                
                                <!-- 國文成績 -->
                                <td class="avg-cell stat-cell">{{ class_data.subjects.chinese.avg }}</td>
                                <td class="highest-cell stat-cell">{{ class_data.subjects.chinese.highest }}</td>
                                <td class="lowest-cell stat-cell">{{ class_data.subjects.chinese.lowest }}</td>
                                
                                <!-- 數學成績 -->
                                <td class="avg-cell stat-cell">{{ class_data.subjects.math.avg }}</td>
                                <td class="highest-cell stat-cell">{{ class_data.subjects.math.highest }}</td>
                                <td class="lowest-cell stat-cell">{{ class_data.subjects.math.lowest }}</td>
                                
                                <!-- 英文成績 -->
                                <td class="avg-cell stat-cell">{{ class_data.subjects.english.avg }}</td>
                                <td class="highest-cell stat-cell">{{ class_data.subjects.english.highest }}</td>
                                <td class="lowest-cell stat-cell">{{ class_data.subjects.english.lowest }}</td>
                            </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
            
            <!-- 圖例說明 -->
            <div class="legend">
                <h3>📋 統計說明</h3>
                <div class="legend-grid">
                    <div class="legend-item">
                        <div class="legend-color avg-cell"></div>
                        <span>平均分數</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-color highest-cell"></div>
                        <span>最高分數</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-color lowest-cell"></div>
                        <span>最低分數</span>
                    </div>
                </div>
                <p style="margin-top: 15px; color: #666; font-size: 0.9em;">
                    💡 提示：此表格支援響應式設計，可在各種裝置上正常顯示
                </p>
            </div>
            
        {% else %}
            <div style="text-align: center; padding: 40px; color: #666;">
                目前沒有班級統計資料
            </div>
        {% endif %}
    </div>
</body>
</html>
```

---

## 解答重點說明

### 題目1 重點
- 使用基本的Django template語法 `{% for %}` 和 `{{ }}`
- 正確的HTML表格結構
- 基礎CSS樣式和hover效果
- 空資料的處理 `{% if %}`

### 題目2 重點
- 條件判斷語法 `{% if %}`, `{% elif %}`, `{% else %}`
- Template filter使用 (`stringformat`, `length`)
- CSS條件格式的實現
- 資料計算和顯示

### 題目3 重點
- 複雜表格結構 (`colspan`, `rowspan`)
- 響應式設計 (`@media` queries)
- 巢狀資料的處理
- 表格的語意化設計
- 可用性和美觀性的平衡

### 學習要點總結
1. **Django Template語法**：熟練使用循環、條件判斷
2. **HTML語意化**：正確使用表格相關標籤
3. **CSS設計**：響應式布局、條件格式、使用者體驗
4. **資料處理**：複雜資料結構的顯示和計算
5. **程式組織**：View和Template的職責分離