#coding=utf-8
from django.shortcuts import redirect
def islogin(Max):
    def Maxce(request, *args, **kwargs):
        #判断是否登陆
        if request.session.has_key('uid'):
            #登陆，执行行Max函数
            return Max(request,*args, **kwargs)
        else:
            #未登录，跳转到login视图
            return redirect('/user/login')
    return Maxce