"""
URL configuration for mblog project.

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
from django.urls import path, include
from mysite.views import homepage, showpost, listing, listing2
from mysite.views import showpost_date, about, about2, about3, disp_detail, about_author
#習題
from mysite.views import student_list, student_grades

about_patterns = [
    path('about2/', about2, name='about2'),
    path('about3/', about3, name='about2'),
    path('about/<int:author_id>/', about_author, name='about_author'),
    path('about/', about_author, name='about_author'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('post/<slug:slug>/', showpost, name='showpost'),
    # path('post/114年/<path:post_date>/', showpost_date, name='showpost_date'),
    # path('post/<path:post_date>/', showpost_date, name='showpost_date'),
    path('list/', listing, name='listing'),
    path('list/<str:id>/', disp_detail, name='listing'),
    # path('list/', listing2, name='listing'),
    # path('about/', about, name='about'),
    path('author/', include(about_patterns)),
    # path('post/<int:yr>/<int:mo>/<int:day>/', showpost_date, name='post_url'),
    path('student/', student_list, name='student_list'),
    path('grade/', student_grades, name='grade_list'),



]

