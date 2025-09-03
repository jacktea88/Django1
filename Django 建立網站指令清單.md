# Django 建立網站指令清單

## 1. 建立與啟用環境

``` bash
conda create -n django_env python=3.10
conda activate django_env
```

## 2. 安裝 Django

``` bash
pip install django
```

（或指定版本）

``` bash
pip install django==4.2
```

## 3. 建立專案
### 建立專案資料夾

``` bash
md 12mshop
cd 12mshop
django-admin startproject mshop
``` 

### 建立app 注意在settings.py中要註冊app
進入剛建立的專案資料夾
``` bash
cd mshop
python manage.py startapp mysite
```

## 4. 啟動開發伺服器

``` bash
cd mysite
python manage.py runserver
```

👉 瀏覽器輸入 <http://127.0.0.1:8000>

## 5. 建立應用 (app)

``` bash
python manage.py startapp blog
```

## 6. 建立資料庫遷移檔

``` bash
python manage.py makemigrations
```

## 7. 執行資料庫遷移

``` bash
python manage.py migrate
```

## 8. 建立管理員帳號

``` bash
python manage.py createsuperuser
```

## 9. 進入 Django Shell

``` bash
python manage.py shell
```

## 10. 匯出需求套件

``` bash
pip freeze > requirements.txt
```
