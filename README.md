# ShortenURL

使用 Django 1.9  
提供簡易縮網址的服務

## 安裝套件

Django==1.9
django-hosts==2.0

## 執行Django

cd path/to/my/project

django-admin.py startproject ShortenURL

### 建立虛擬環境

virtualenv . 

source bin/active

### 模型與資料庫之同步

1. 建立migration資料檔，如果模型有任何異動，則會產生新的migration檔

    python manage.py makemigrations

2. migrate會根據指定的migration記錄(利用編號指定)去將模型同步到資料庫

    python manage.py migrate

### 創立 superuser

python manage.py createsuperuser

### 接著就可以跑看看了

python manage.py runserver


