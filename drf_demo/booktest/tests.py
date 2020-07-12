# 设置Django运行所依赖的环境变量
import os

if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_demo.settings')

# 让Django进行一次初始化
import django

django.setup()

from booktest.models import BookInfo, HeroInfo
from booktest.serializers import BookInfoSerializer, HeroInfoSerializer
from rest_framework import serializers
import json


class User(object):
    '''用户类'''

    def __init__(self, name, age):
        self.name = name
        self.age = age


class UserSerializer(serializers.Serializer):
    '''用户序列化器类'''
    name = serializers.CharField()
    # 注：一旦一个字段设置了default，则这个字段的required默认为False
    age = serializers.IntegerField(default=20)


if __name__ == '__main__':
    # 获取一本书
    book = BookInfo.objects.get(id=9)

    # 准备数据
    req_data = {'btitle': 'django_rest', 'bpub_date': '2019-06-01', 'bread': 21, 'bcomment': 20}

    # 创建序列化器对象
    serializer = BookInfoSerializer(book, data=req_data)

    # 数据校验
    serializer.is_valid()

    # 数据保存：此处save会调用序列化器类中的create方法
    serializer.save()

    # 获取create方法返回的对象序列化之后的数据
    res = serializer.data
    res = json.dumps(res, indent=1, ensure_ascii=False)
    print(res)

    # # 查询获取图书对象
    # book = BookInfo.objects.all()
    #
    # # 创建序列化对象
    # serializer = BookInfoSerializer(book,many=True)
    #
    # # 获取序列化之后的数据
    # res = serializer.data
    #
    # # 数据格式化显示
    # res = json.dumps(res, indent=1, ensure_ascii=False)
    # print(res)
