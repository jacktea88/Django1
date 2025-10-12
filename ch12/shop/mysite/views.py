from django.shortcuts import redirect, render
from mysite import forms, models
from django.contrib.sessions.models import Session
from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# for votes
from mysite.models import Vote

# use plotly
# from plotly.offline import plot
# import plotly.graph_objs as go

# for temperature
from mysite.models import Temperature
import json
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt    

# for cart
from cart.cart import Cart

# for order
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
# def index(request):
#     if request.session.test_cookie_worked():
#         request.session.delete_test_cookie()
#         message = 'Cookie 已成功啟用'
#     else:
#         message = 'Cookie 啟用失敗'
#         request.session.set_test_cookie()
#     return render(request, 'index.html', locals())

# 檢查username是否存在
# def index(request):
#     if 'username' in request.session:
#         username = request.session['username']
#         print('username:in index', username)
#         # message = '登入成功'
#         messages.info(request, '登入成功')
#     else:
#         username = None
#         print('username不存在')
#         # message = '登入失敗'
#         messages.warning(request, '登入失敗')
#     return render(request, 'index.html', locals())

# use django auth for index
def index(request):
    all_products = models.Product.objects.all()
    test = 'test'
    print('all_products:', all_products)
    print('test:', test)
    if request.user.is_authenticated:
        username = request.user.username
        print('username:in index', username)
        # message = '登入成功'
        messages.info(request, '登入成功')
    else:
        username = None
        print('username不存在')
        # message = '登入失敗'
        messages.warning(request, 'USER不存在，登入失敗')
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
#                     messages.warning(request, '成功登入了')
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

# use django auth login
def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name=request.POST['username'].strip()
            login_password=request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
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

# session logout
def logout(request):
    if 'username' in request.session:
        Session.objects.all().delete()
        # del request.session['username']
        print('登出成功')
        # message = '登出成功'
        messages.warning(request, '登出成功')
    return redirect('/')

# user info from session
# def userinfo(request):
#     if 'username' in request.session:
#         username = request.session['username']
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

# use django auth userinfo
@login_required(login_url='/login/')
def userinfo(request):
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email
        print('username:in userinfo', username)
    else:
        print('username不存在')
        return redirect('/login/')
    try:
        user = User.objects.get(username=username)
        userinfo = models.Profile.objects.get(user=user)    # 用自己擴充的Profile欄位
        # userinfo = models.User.objects.get(name=username) # 用自己的User欄位
        # userinfo = User.objects.get(username=username)     # 用auth內建的User欄位
        # userinfo = models.Profile.objects.get(user=user)
    except Exception as e:
        print(e)
        pass
    return render(request, 'userinfo.html', locals())

# use django auth logout
def logout(request):
    auth.logout(request)
    messages.warning(request, '登出成功')
    return redirect('/')

# for product detail
def product(request, id):   # id是product的id，不處理id=0，也不處理不存在的id，一律返回None
    try:
        product = models.Product.objects.get(id=id)
    except:
        product = None

    return render(request, 'product.html', locals())

# for add to cart
@login_required
def add_to_cart(request, id, quantity):
    cart = Cart(request)
    product = models.Product.objects.get(id=id)
    cart.add(product=product, quantity=quantity)

    return redirect('/')

# for remove from cart
@login_required
def remove_from_cart(request, id):
    product = models.Product.objects.get(id=id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('/cart/')

# for cart detail
@login_required
def cart_detail(request):
    all_categories = models.Category.objects.all()
    cart = Cart(request).cart # 這裡是取得購物車所有的商品
    #Cart(request) 會回傳一個 Cart 實例，而 .cart 則是取得該實例中的購物車物件。

    print(cart)

    total_price = 0
    for _, item in cart.items(): # item是一個字典，_ 是一個常見的Python慣例，代表一個不需要使用的變數(id），而 item 則是代表每個商品項目。
        current_price = float(item['price']) * int(item['quantity'])
        total_price += current_price

    return render(request, 'cart.html', locals())

# for order
# @verified_email_required
def order(request):
    all_categories = models.Category.objects.all()
    cartInstance = Cart(request)
    cart = cartInstance.cart
    total_price = 0
    for _, item in cart.items():
        current_price = float(item['price']) * int(item['quantity'])
        total_price += current_price
    
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        new_order = models.Order(user=user)

        form = forms.OrderForm(request.POST, instance=new_order)
        if form.is_valid():
            order = form.save()
            email_messages = "您的購物內容如下:\n"
            for _, item in cart.items(): # item是一個字典，_ 是一個常見的Python慣例，代表一個不需要使用的變數(id），而 item 則是代表每個商品項目。
                product = models.Product.objects.get(id=item['product_id'])
                models.OrderItem.objects.create(
                    order=order, 
                    product=product,
                    price = item['price'],
                    quantity=item['quantity']
                )
                email_messages = email_messages + "\n" + \
                                "{}, {}, {}".format(item['name'], \
                                item['price'], item['quantity'])
            email_messages = email_messages + \
                            "\n總金額為:" + str(total_price)
            #清空購物車
            cartInstance.clear()
            messages.success(request, '訂單已成立，謝謝您的購買')

            #寄送訂單給客戶
            send_mail(
                '訂單已成立，謝謝您的購買',  # email標題
                email_messages,  # email內容
                settings.EMAIL_HOST_USER,  # 寄件人
                [user.email],  # 收件人(客戶)
            )
            #寄送訂單通知給管理員
            send_mail(
                '有訂單成立通知',  # email標題
                email_messages,  # email內容
                settings.EMAIL_HOST_USER,  # 寄件人
                [settings.EMAIL_HOST_USER],  # 收件人(管理員)
            )
            #跳轉user訂單頁面
            return redirect('/myorders/')
    else:   # 如果是 GET 請求
        form = forms.OrderForm()

    return render(request, 'order.html', locals())

# for myorders
@login_required
def my_orders(request):
    all_categories = models.Category.objects.all()
    orders = models.Order.objects.filter(user=request.user)

    return render(request, 'myorders.html', locals())