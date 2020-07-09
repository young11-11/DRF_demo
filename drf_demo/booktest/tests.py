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
    # 此处age字段的required参数默认为True
    age = serializers.IntegerField(required=False)
    addr = serializers.CharField(default='默认地址')



if __name__ == '__main__':

    # 准备数据：此数据在实际中经常是客户端传递的，此处只是模拟

    # 为user对象传值
    user = User('张云龙',18)

    # 将对象传入，进行序列化
    serializer = UserSerializer(user)

    print(serializer.data)