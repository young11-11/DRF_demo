# 设置Django运行所依赖的环境变量
import os

if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_demo.settings')

# 让Django进行一次初始化
import django

django.setup()

from rest_framework import serializers


class User(object):
    '''用户类'''

    def __init__(self, name, age):
        self.name = name
        self.age = age


class UserSerializer(serializers.Serializer):
    '''用户序列化器类'''
    name = serializers.CharField()
    age = serializers.ImageField()


if __name__ == '__main__':

    # 准备数据：此数据在实际中经常是客户端传递的，此处只是模拟

    data = {'name': '张云龙', 'age': 30}

    # 创建序列化器对象，传入待校验的数据
    serializer = UserSerializer(data=data)

    # 调用is_valid进行数据校验，成功返回True，失败返回False
    res = serializer.is_valid()

    if res:
        # 校验通过，获取校验之后的数据
        print("校验通过", serializer.validated_data)
    else:
        # 校验失败，获取错误提示信息
        print('校验失败：', serializer.errors)
