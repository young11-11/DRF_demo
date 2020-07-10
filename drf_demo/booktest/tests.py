# 设置Django运行所依赖的环境变量
import json
import os

if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_demo.settings')

# 让Django进行一次初始化
import django

django.setup()

from booktest.models import BookInfo, HeroInfo
from booktest.serializers import BookInfoSerializer, HeroInfoSerializer
from rest_framework import serializers


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
    # 查询获取图书对象
    book = BookInfo.objects.get(id=2)

    # 创建序列化对象
    serializer = BookInfoSerializer(book)

    # 获取序列化之后的数据
    res = serializer.data

    # 数据格式化显示
    res = json.dumps(res, indent=1, ensure_ascii=False)
    print(res)
