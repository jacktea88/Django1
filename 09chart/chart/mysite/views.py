from django.shortcuts import render
from mysite.models import Vote

# Create your views here.
def votes(request):
    data = Vote.objects.all()
    # data = Vote.objects.all().order_by('name')
    return render(request, 'votes.html', locals())