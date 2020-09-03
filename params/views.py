from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
import os
# Create your views here.
USER_LIST = [
    {"username": "张三", "email": "12@qq.com"}
]
def login(request):
    error_msg = ''
    if request.method == 'POST':
        # 获取用户通过post提交的数据
        user = request.POST['user']
        pwd = request.POST['pwd']
        text = request.POST
        # radio
        print(text.get('sex'))
        # checkbox
        print(text.getlist('favi'))
        # select
        print(text.getlist('city'))
        # file name--文件名  chunks--迭代生成器
        file = request.FILES.get('fff')
        print(file.name)
        with open(os.path.join('upload', file.name), mode='wb') as f:
            for i in file.chunks():
                f.write(i)
        if user == "root" and pwd == 'admin':
            return redirect('/home/')
        else:
            error_msg = '用户名或密码错误'
    return render(request, "login.html", {'error_msg': error_msg})

def home(request):
    if request.method == 'POST':
        USER_LIST.append({"username": request.POST['username'], "email": request.POST['email']})
    return render(request, 'home.html', {"user_list": USER_LIST})