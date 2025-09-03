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
    return render(request, 'twtv.html', locals())