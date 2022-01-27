from django.shortcuts import render ,HttpResponse,redirect  # 添加三板斧H...

# Create your views here.

def index(request):
    """
    param request: 请求相关的所有数据对象 比之前的env更牛
    """

    # return HttpResponse("你好啊 我是django")
    # return render(request,'myfirst.html')  # 自动去templates文件夹下查找文件
    #return redirect('https://www.mzitu.com/')
    return redirect('/home/')  # index跳到home

def home(request):
    return HttpResponse('home')