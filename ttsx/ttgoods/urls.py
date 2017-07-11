#coding=utf-8
from django.conf.urls import url
import views
urlpatterns = [
    url(r'^$', views.index),#商品首页
    url(r'^list(\d+)_(\d+)/$', views.goodslist),#商品列表页
    url(r'^(\d+)/$', views.detail),#商品详细页

]