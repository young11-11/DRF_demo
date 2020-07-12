import json

from django.http import JsonResponse, HttpResponse, Http404
from django.views import View
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import   ReadOnlyModelViewSet
from rest_framework.viewsets import  ModelViewSet

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer


class BookInfoViewSet(ReadOnlyModelViewSet):
    # 指定序列化器类
    serializer_class = BookInfoSerializer
    # 指定视图集
    queryset = BookInfo.objects.all()

    # 指定当前视图自己的认证方案，不再使用全局认证方案
    authentication_classes = [SessionAuthentication]

    # 指定当前视图自己的权限控制方式，不再使用全局权限控制方式
    permission_classes = [IsAuthenticated]



# list：获取一组数据的通用代码
# create：新增一个数据的通用代码
# retrieve：检索、获取，获取指定数据的通用代码
# update：修改指定数据的通用代码
# destroy：摧毁、删除，删除指定数据的通用代码
