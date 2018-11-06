from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import time,paramiko


def ssh_command(hostname, port, user, password, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, port, user, password)
    except:
        return "连接建立失败，请检查服务器信息是否正确！！！"
    stdin, stdout, stderr = ssh.exec_command(cmd)
    result = stdout.readlines()
    if not result:
        result = stderr.readlines()
    ssh.close()
    result = ''.join(result)
    result="<pre>"+result+"</pre>"
    return result

def index(request):
    context = {}
    context['hello'] = "hello,张伟伟！"
    context['date'] = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return render(request, 'index.html', context)
def command(request):
    request.encoding = 'utf-8'
    hostname=request.GET.get("hostname")
    port='22'
    user='root'
    password='123456'
    cmd=request.GET.get("cmd")
    info=ssh_command(hostname, port, user, password, cmd)
    return HttpResponse(info)
