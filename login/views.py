from django.shortcuts import render,redirect
from . import models

# Create your views here.
def index(request):
    pass
    return render(request, 'login/index.html')


def  login(request):
    print(request.method)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        message = "所有字段都必须填写！"
        if username and password:
            try:
                user = models.User.objects.get(username=username)
                if user.password == password:
                    return redirect('/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！！"
        return render(request, 'login/login.html', {"message": message})
    return render(request, 'login/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return render(request, 'login/logout.html')

