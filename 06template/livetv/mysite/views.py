from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    msg = 'Hello, LiveTV'
    now = datetime.now()

    return render(request, 'index.html', locals())

def twtv(request, tv_id=0):
    tv_list = [{'name':'公視', 'tvcode':'quwqlazU-c8'},
        {'name':'非凡', 'tvcode':'eA6Aczd3FZM'},
        {'name':'民視', 'tvcode':'ylYJSBUgaMA'},
        {'name':'中視', 'tvcode':'TCnaIE_SAtM'},]
    tv = tv_list[tv_id]
    now = datetime.now()
    # hour = now.timetuple().tm_hour
    hour = now.hour
    # print(f'hour: {hour} now: {now}')
    return render(request, 'twtv.html', locals())

def engtv(request, tv_id=0):
    tv_list = [{'name':'ABC', 'tvcode':'quwqlazU-c8'},
        {'name':'CBS', 'tvcode':'eA6Aczd3FZM'},
        {'name':'NBC', 'tvcode':'ylYJSBUgaMA'},
        {'name':'CNN', 'tvcode':'TCnaIE_SAtM'},]
    tv = tv_list[tv_id]
    now = datetime.now()
    return render(request, 'engtv.html', locals())


# execercise
def home(request):

    return render(request, 'home_all.html', locals())
    return render(request, 'home.html', locals())

def about(request):
    
    return render(request, 'about_test.html', locals())
    return render(request, 'about.html', locals())

def services(request):
    
    return render(request, 'services_all.html', locals())
    return render(request, 'services.html', locals())

def contact(request):
    
    return render(request, 'contact.html', locals())

def contact_all(request):
    return render(request, 'contact_test.html', locals())
    return render(request, 'contact_all.html', locals())

def login(request):
    
    return render(request, 'login.html', locals())

def register(request):
    
    return render(request, 'register.html', locals())