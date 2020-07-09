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
    age = serializers.ImageField(write_only=True)


if __name__ == '__main__':

    # 准备数据：此数据在实际中经常是客户端传递的，此处只是模拟

    user = User('张云龙',18)

    # 将user对象序列化为字典{'name': '张云龙', 'age': 18}
    serializer = UserSerializer(user)

    print(serializer.data)
