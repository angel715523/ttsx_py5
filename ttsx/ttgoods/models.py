#coding=utf-8
from django.db import models
from tinymce.models import HTMLField
# 商品分类
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=10)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle.encode('utf-8')

# 商品类
class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)#标题
    gpic = models.ImageField(upload_to='goods/')#图片
    gprice = models.DecimalField(max_digits=5,decimal_places=2)#单价，最大5位数，保留2位小数
    gclick = models.IntegerField()  # 点击量
    gunit = models.CharField(max_length=10)#单位
    isDelete = models.BooleanField(default=False)
    gsubtitle = models.CharField(max_length=100)#副标题
    greserve = models.IntegerField(default=100)#库存
    gcontent = HTMLField()  # 商品详情，富文本编辑
    gtype = models.ForeignKey('TypeInfo')