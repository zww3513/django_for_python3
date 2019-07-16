from django.shortcuts import render,redirect
from . import models
from .forms import UserForm

# Create your views here.
def index(request):
    pass
    return render(request, 'login/index.html')


def  login(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "所有字段都必须填写！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(username=username)
                if user.password == password:
                    return redirect('/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！！"
        return render(request, 'login/login.html', locals())
    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return render(request, 'login/logout.html')

