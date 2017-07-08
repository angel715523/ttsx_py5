#coding=utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse
from models import UserInfo
from hashlib import sha1
import datetime
import user_decorators

# 注册页面
def register(request):
    content = {'title':'注册页面', 'top':'0'}
    return render(request, 'ttusers/register.html', content)
# 注册页面连接数据库
def register_handle(request):
    # 接收用户请求
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    #ucpwd = post.get('user_cpwd')
    umail = post.get('user_email')
    # 密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()
    # 向数据库中保存数据
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_sha1
    #user.ucpwd = ucpwd
    user.umail = umail
    user.save()
    #重定向到登陆页面
    return redirect('/user/login/')
#重名检测
def register_copy(request):
    #接收用户名
    username = request.GET.get('uname')
    #username = request.POST.get('uname')
    #查询当前个数
    copy = UserInfo.objects.filter(uname=username).count()
    #返回json{'haha':1或0}
    content = {'haha':copy}
    return JsonResponse(content)

#登陆页面
def login(request):
    #login_handle判断记住用户名选项是否勾选返回给rember
    rember = request.COOKIES.get('uname', '')
    content = {'title':'登陆页面', 'uname':rember, 'top':'0'}
    return render(request, 'ttusers/login.html', content)
#登陆页面连接数据库
def login_handle(request):
    #接收用户请求
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    ureb = post.get('user_rember', '1')#表示{'user_rember':'value'}
    #密码加密匹配
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()
    content = {'title':'登陆页面', 'uname':uname, 'upwd':upwd, 'top':'0'}
    #用户名判断
    # 如果没有查到数据则返回[]，如果查到数据则返回[UserInfo对象]
    result = UserInfo.objects.filter(uname=uname)
    if len(result) == 0:
        # 用户名不存在
        content['error_name'] = '用户名错误'
        return render(request, 'ttusers/login.html', content)
    else:
        # 用户名存在
        if result[0].upwd == upwd_sha1:
            # 密码正确，登陆成功。添加中间件，例如在列表页点登陆，登陆后跳回列表页（‘/’默认跳转index）
            response = redirect(request.session.get('url_path', '/'))
            #response = redirect('/user/')
            #在session中保存用户名编号，用于记录用户对应信息
            request.session['uid'] = result[0].id
            #右上角欢迎中显示是那个用户登陆
            request.session['uname'] = result[0].uname
            #记住用户名,这里的1是判断是否跟模板中的value是否相等
            if ureb == '1':
                #基于当前时间加过期时间（加了14天）
                response.set_cookie('uname', uname, expires = datetime.datetime.now() + datetime.timedelta(days = 14))
            #不勾选立即过期
            else:
                response.set_cookie('uname', uname, max_age = -1)
            return response
        else:
            # 密码错误
            content['error_pwd'] = '密码错误'
            return render(request, 'ttusers/login.html', content)
#退出登陆,返回登陆页面
def logout(request):
    request.session.flush()
    return redirect('/user/login/')

#用户中心
@user_decorators.islogin
def center(request):
    user =UserInfo.objects.get(pk = request.session['uid'])
    content = {'title':'用户中心', 'user':user}
    return render(request, 'ttusers/center.html', content)
#订单
@user_decorators.islogin
def order(request):
    content = {'title':'全部订单'}
    return render(request, 'ttusers/order.html', content)
#收货地址
@user_decorators.islogin
def site(request):
    user = UserInfo.objects.get(pk = request.session['uid'])
    if request.method == 'POST':  # post请求，修改当前用户对象的收货信息
        # 接收用户请求
        post = request.POST
        uman = post.get('uman')
        address = post.get('uaddress')
        ucode = post.get('ucode')
        uphone = post.get('uphone')
        # 向数据库中保存数据
        user.uman = uman
        user.uaddress = address
        user.ucode = ucode
        user.uphone = uphone
        user.save()
    content = {'title':'收货地址', 'info':user}
    return render(request, 'ttusers/site.html', content)

def index(request):
    content = {}
    return render(request, 'index.html', content)




