import json

from django.http import JsonResponse, HttpResponse, Http404
from django.views import View
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins

from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from rest_framework.throttling import AnonRateThrottle

from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        """判断对使用此权限类的视图是否有访问权限"""
        # 任何用户对使用此权限类的视图都有访问权限
        return True

    def has_object_permission(self, request, view, obj):
        """判断对使用此权限类视图中的某个数据对象是否有访问权限"""
        # 需求: 对id为1，3的数据对象有访问权限
        if obj.id in (1, 3):
            return True
        return False


class BookInfoViewSet(ReadOnlyModelViewSet):
    # 指定序列化器类
    serializer_class = BookInfoSerializer
    # 指定视图集
    queryset = BookInfo.objects.all()

    # 指定当前视图自己的认证方案，不再使用全局认证方案
    authentication_classes = [SessionAuthentication]

    # 使用自定义的权限控制类
    permission_classes = [MyPermission]

    # 此时设置当前视图仅针对匿名用户进行限流控制
    # throttle_classes = [AnonRateThrottle]

    # 此处指定当前视图采用contacts限流频次进行限流
    throttle_scope = 'contacts'


# list：获取一组数据的通用代码
# create：新增一个数据的通用代码
# retrieve：检索、获取，获取指定数据的通用代码
# update：修改指定数据的通用代码
# destroy：摧毁、删除，删除指定数据的通用代码
