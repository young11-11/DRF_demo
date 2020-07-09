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
    def __init__(self,name,age):
        self.name = name
        self.age = age


class UserSerializer(serializers.Serializer):
    '''用户序列化器类'''
    name = serializers.CharField()
    age = serializers.ImageField()



if __name__ == '__main__':

    '''创建user对象'''
    user = User(name="张云龙",age=18)


    # 创建序列化器对象，传入被序列化的user对象
    # serializer = UserSerializer(instance=user)

    serializer = UserSerializer(user)

    # 获取序列化之后的数据

    res = serializer.data
    print(res)











