#coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^register/$', views.register),# 注册页面
    url(r'^register_handle/$', views.register_handle),#注册页保存数据
    url(r'^register_copy/$', views.register_copy),#注册页重名检测
    url(r'^login/$', views.login),#登陆页面
    url(r'^login_handle/$', views.login_handle),#登陆页面验证数据
    url(r'^center/$', views.center),#用户中心
    url(r'^order/$', views.order),#订单
    url(r'^site/$', views.site),#收货地址
    url(r'^logout/$', views.logout),#退出登陆
    #url(r'^$', views.index),

]