from django.shortcuts import render, HttpResponse
from mysite.models import Vote, Temperature
from plotly.offline import plot
import plotly.graph_objs as go
# import numpy as np
from django.views.decorators.csrf import csrf_exempt
import json

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

# 使用ploty來繪製溫度圖表
def plotly_mqtt(request):
    data = Temperature.objects.all().order_by('-id')[:20]
    x = [d.created_at for d in data]
    y = [d.temperature for d in data]
    trace = go.Scatter(x=x, y=y, name='溫度', mode='lines+markers')
    layout = go.Layout(title='溫度數據', height=500)
    fig = go.Figure(data=[trace], layout=layout)
    temp_div = plot(fig, output_type='div')
    return render(request, 'temp.html', locals())

@csrf_exempt
def plotly_api(request):
    #接收前端sendTemperatureToBackend(temperature), 
    # 接收XMLHttpRequest()傳來的資料
    print('request.body:', request.body)
    # print('request.POST:', request.POST)
    # print('request:', request)
    if request.body :
        

        data = json.loads(request.body.decode('utf-8'))
        print('json data:', data)
        # temperature = int(data['temperature'])
        temperature = data['temperature']
        
    else : 
        temperature = 0
    print(temperature)
    # 儲存溫度數據到資料庫
    temp = Temperature(temperature=temperature)
    temp.save()
    print('溫度數據已儲存到資料庫')

    return HttpResponse(temperature)
    return render(request, 'mqtt.html', locals())

def mqtt_show(request):
    return render(request, 'mqtt.html', locals())