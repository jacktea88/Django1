from django.shortcuts import render
from mysite.models import Vote
from plotly.offline import plot
import plotly.graph_objs as go
# import numpy as np

# Create your views here.
def votes(request):
    data = Vote.objects.all()
    # data = Vote.objects.all().order_by('name')
    return render(request, 'votes.html', locals())

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
