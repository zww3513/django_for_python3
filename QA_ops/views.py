from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import time

def index(request):
    context = {}
    context['hello'] = "hello,张伟伟！"
    context['date'] = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return render(request, 'index.html', context)
def command(request):
    request.encoding = 'utf-8'
    info="serverIp="+request.GET['serverIp']+"<br>"
    info=info+"command="+request.GET['command']
    print(info)
    return HttpResponse(info)
