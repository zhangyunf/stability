from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
import os
# Create your views here.
USER_LIST = [
    {"username": "张三", "email": "12@qq.com"}
]

USER_LIST_1 = {
    "1": {'name': 'root1', 'email': 'root@1.com'},
    "2": {'name': 'root2', 'email': 'root@2.com'},
}
# FBV
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
        if file:
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

def index(request):
    return render(request, 'index.html', {"user_list_1": USER_LIST_1})

def detail(request, nid):
    return HttpResponse(nid)
    # detail_info = USER_LIST_1[nid]
    # return render(request, 'detail.html', {"detail_info": detail_info})
# CBV
from django.views import View
class Login(View):
    def dispatch(self, request, *args, **kwargs):

        return super(Login, self).dispatch(request, *args, **kwargs)


    def get(self, request):
        print("get")
        return render(request, "login.html")

    def post(self, request):
        print("post")
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
            if file:
                with open(os.path.join('upload', file.name), mode='wb') as f:
                    for i in file.chunks():
                        f.write(i)

            if user == "root" and pwd == 'admin':
                return redirect('/home/')
            else:
                error_msg = '用户名或密码错误'
        return render(request, "login.html", {'error_msg': error_msg})