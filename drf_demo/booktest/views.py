import json

from django.http import JsonResponse, HttpResponse, Http404
from django.views import View
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer


class BookInfoViewSet(ModelViewSet):

    # 指定序列化器类
    serializer_class = BookInfoSerializer
    # 指定视图集
    queryset = BookInfo.objects.all()



# list：获取一组数据的通用代码
# create：新增一个数据的通用代码
# retrieve：检索、获取，获取指定数据的通用代码
# update：修改指定数据的通用代码
# destroy：摧毁、删除，删除指定数据的通用代码
