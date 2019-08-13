from django.shortcuts import render,redirect
from . import models
from django.http import JsonResponse

def server(request):
    pass
    return render(request, 'asset/server.html')



def group_config(request):
    pass
    return render(request, 'asset/group_config.html')