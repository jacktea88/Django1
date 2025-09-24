from django.shortcuts import render, HttpResponse, redirect
from mysite import models, forms
from django.contrib.sessions.models import Session
from django.contrib import messages

# use django auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from mysite.models import Vote, Temperature
from plotly.offline import plot
import plotly.graph_objs as go
# import numpy as np
from django.views.decorators.csrf import csrf_exempt
import json

# 測試cookie是否啟用
# def index(request):
#     if request.session.test_cookie_worked():
#         request.session.delete_test_cookie()
#         message = 'Cookie 已成功啟用'
#     else:
#         message = 'Cookie 啟用失敗'
#         request.session.set_test_cookie()
#     return render(request, 'index.html', locals())

# 檢查'username'有沒有存在於Session中, 如果有就把username以及useremail都取出來
# def index(request):
#     if 'username' in request.session and request.session['username'] != None:
#         username = request.session['username']
#         useremail = request.session['useremail']
#         print('username:in index', username)
#     else:
#         print('username不存在')
#     return render(request, 'index.html', locals())

#use django auth
def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email
        messages.get_messages(request)
        print('username:in index', username)
    else:
        print('username不存在 by index')
    return render(request, 'index.html', locals())


# def login(request):
#     if request.method == 'POST':
#         login_form = forms.LoginForm(request.POST)
#         if login_form.is_valid():
#             login_name=request.POST['username'].strip()
#             login_password=request.POST['password']
#             print('login_name:', login_name)
#             try:
#                 user = models.User.objects.get(name=login_name)
#                 if user.password == login_password:
#                     request.session['username'] = login_name
#                     request.session['useremail'] = user.email
#                     return redirect('/')
#                 else:
#                     # message = '密碼錯誤'
#                     messages.warning(request, '密碼錯誤')
#             except:
#                 # message = '找不到使用者'
#                 messages.warning(request, '找不到使用者')
#         else:
#             # message = '請檢查輸入的欄位內容'
#             messages.warning(request, '請檢查輸入的欄位內容')
#     else:   # GET
#         login_form = forms.LoginForm()
#     return render(request, 'login.html', locals())


# use django auth
def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name=request.POST['username'].strip()
            login_password=request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
                    # login(request, user)
                    auth.login(request, user)
                    messages.warning(request, '成功登入了')
                    return redirect('/')
                else:
                    messages.warning(request, '帳號尚未啟用')
            else:
                messages.warning(request, '登入失敗')
        else:
            messages.warning(request, '請檢查輸入的欄位內容')
    else:   # GET
        login_form = forms.LoginForm()
    return render(request, 'login.html', locals())


# def logout(request):
#     if 'username' in request.session:

#         Session.objects.all().delete()
#         # 指定刪除的session寫法
#         # del request.session['username']
#         # del request.session['useremail']
#     return redirect('/')

# use django auth
def logout(request):
    auth.logout(request)
    messages.warning(request, '成功登出了')
    return redirect('/')


# def userinfo(request):
#     if 'username' in request.session:
#         username = request.session['username']
#         useremail = request.session['useremail']
#         print('username:in userinfo', username)
#     else:
#         print('username不存在')
#         return redirect('/login/')
#     try:
#         userinfo = models.User.objects.get(name=username)
#     except Exception as e:
#         print(e)
#         pass
#     return render(request, 'userinfo.html', locals())

# use django auth
@login_required(login_url='/login/')
def userinfo(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            user = User.objects.get(username=username)
            userinfo = models.Profile.objects.get(user=user)    # 用profile增加user欄位，這樣可以把user額外的資訊帶出來
            # userinfo = User.objects.get(username=username)     # 用auth內建的User欄位，沒有增加user欄位
            # userinfo = models.User.objects.get(username=username)
        except Exception as e:
            print(e)
            pass
    return render(request, 'userinfo.html', locals())

# Create your views here.
def votes(request):
    # data = Vote.objects.all()
    data = Vote.objects.all().order_by('name')
    return render(request, 'votes.html', locals())
    # return render(request, 'votes_table.html', locals())


def plotly(request):
    data = Vote.objects.all()
    # data = Vote.objects.all().order_by('name')
    x = [d.votes for d in data]
    y = [d.name for d in data][::-1]
    trace = go.Bar(x=x, y=y, name='2022', orientation='h')
    layout = go.Layout(title='2022年高雄市左楠區市議員選舉得票數',
                       height=500)
    fig = go.Figure(data=[trace], layout=layout)
    plot_div = plot(fig, output_type='div')
    return render(request, 'plotly.html', locals())

# 使用ploty來繪製溫度圖表
def plotly_mqtt(request):
    data = Temperature.objects.all().order_by('-id')[:10]
    # data = Temperature.objects.all()
    x = [d.created_at for d in data]
    y = [d.temperature for d in data]
    trace = go.Scatter(x=x, y=y, name='溫度', mode='lines+markers')
    layout = go.Layout(title='溫度數據', height=500)
    fig = go.Figure(data=[trace], layout=layout)
    temp_div = plot(fig, output_type='div')
    return render(request, 'temp.html', locals())

@csrf_exempt
def plotly_api(request):
    if request.body:
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        temperature = data['temperature']
    else:
        temperature = 0
    temp = Temperature(temperature=temperature)
    temp.save()
    return HttpResponse(temperature)
    return render(request, 'mqtt.html', locals())

# @csrf_exempt
# def plotly_api(request):
#     #接收前端sendTemperatureToBackend(temperature), 
#     # 接收XMLHttpRequest()傳來的資料
#     print('request.body:', request.body)
#     # print('request.POST:', request.POST)
#     # print('request:', request)
#     if request.body :
#         data = json.loads(request.body.decode('utf-8'))
#         print('json data:', data)
#         # temperature = int(data['temperature'])
#         temperature = data['temperature']
#     else : 
#         temperature = 0
#     print(temperature)
#     # 儲存溫度數據到資料庫
#     temp = Temperature(temperature=temperature)
#     temp.save()
#     print('溫度數據已儲存到資料庫')
#     return HttpResponse(temperature)
#     return render(request, 'mqtt.html', locals())


def mqtt_show(request):
    return render(request, 'mqtt.html', locals())