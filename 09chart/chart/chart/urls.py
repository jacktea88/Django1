"""
URL configuration for chart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite.views import votes, plotly, plotly_api, mqtt_show, plotly_mqtt, index, login, logout, userinfo

# 設定admin登入頁面標題
admin.site.site_header = '我的網站header'
admin.site.site_title = '我的網站site title'
admin.site.index_title = '後台管理index title'

urlpatterns = [
    path('', index, name='home'),
    path('login/', login, name='index'),
    path('logout/', logout, name='logout'),
    path('userinfo/', userinfo, name='userinfo'),
    path('admin/', admin.site.urls),
    path('votes/', votes, name='votes'),
    path('plotly/', plotly, name='plotly'),
    path('api/temperature/', plotly_api, name='plotly_api'),
    path('mqtt/', mqtt_show, name='mqtt_show'),
    path('temp/', plotly_mqtt, name='plotly_mqtt'),
]
