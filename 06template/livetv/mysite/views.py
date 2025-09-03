from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    msg = 'Hello, LiveTV'
    now = datetime.now()
    return render(request, 'index.html', locals())