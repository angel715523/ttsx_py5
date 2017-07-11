#coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
# 商品首页
def index(request):
    # 查询分类
    type_list = TypeInfo.objects.all()
    list1 = []
    for xx in type_list:
        new_list = xx.goodsinfo_set.order_by('-id')[0:4]#最新商品
        click_list = xx.goodsinfo_set.order_by('-gclick')[0:4]#点击量最高商品
        list1.append({'new_list':new_list, 'click_list':click_list, 'tt':xx})
    context = {'list1':list1, 'title':'首页', 'cart_show':1}
    return render(request, 'ttgoods/index.html', context)

#列表页
def goodslist(request, tid, pindex):
    #查找分类对象
    object = TypeInfo.objects.get(pk = int(tid))
    new_list = object.goodsinfo_set.order_by('-id')[0:2]#新品排序
    glist = object.goodsinfo_set.order_by('-id')#商品排序
    # 商品分页
    p = Paginator(glist, 15)
    page = p.page(int(pindex))
    context = {'title':'商品列表', 'tt':object, 'cart_show':1, 'news':new_list, 'page':page}
    return render(request, 'ttgoods/list.html', context)

#详细页
def detail(request, id):
    #查询是会报异常，但不影响结果，只需要顺利执行就好
    try:
        #获取商品的id，找到对应TypeInfo关系的gtype属性降序获取所有商品
        gidd = GoodsInfo.objects.get(pk = int(id))
        #找到当前商品的分类对象，再找到所有此分类的商品中最新的两个
        new_list = gidd.gtype.goodsinfo_set.order_by('-id')[0:2]
        context = {'title':'商品详情', 'cart_show':1,'news':new_list, 'goods':gidd}
        return render(request, 'ttgoods/detail.html', context)
    except:
        return render(request, '404.html')




