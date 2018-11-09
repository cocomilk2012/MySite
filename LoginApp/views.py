from LoginApp import models
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        name = request.POST.get('txt_username')
        pwd = request.POST.get('txt_pwd')
        if name == 'root' and pwd == '123123':
            redirect('http://www.baidu.com/')
            models.UserInfo.objects.create(UserName=name, UserPwd=pwd)
            user_lists = models.UserInfo.objects.all()
            return render(request, 'index.html', {'msg': '登录成功', 'data': user_lists})
        else:
            return render(request, 'index.html', {'msg': '账号或密码错误'})
