from django.shortcuts import render,redirect
from . import models
from .forms import UserForm
from .forms import RegisterForm
# Create your views here.
def index(request):
    pass
    return render(request, 'login/index.html')


def  login(request):
    if request.session.get('is_login',None):
        return redirect('/')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "所有字段都必须填写！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(username=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！！"
        return render(request, 'login/login.html', locals())
    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            role = register_form.cleaned_data['role']
            nickname = register_form.cleaned_data['nickname']
            print("u:%s\np:%s\nr:%s\nn:%s" % (username, password1, role, nickname))
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(username=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())


                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.username = username
                new_user.password = password1
                new_user.role = int(role)
                print(type(new_user.role))
                new_user.nickname = nickname
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    return redirect("/index/")

