import json

from django.db import DatabaseError
from django.http import JsonResponse, HttpResponse, Http404
from django.views import View
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins

from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from rest_framework.throttling import AnonRateThrottle

from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer



class StandardResultPagination(PageNumberPagination):

    # 指定分页的默认页容量
    page_size = 3
    # 获取分页数据时，页容量参数的名称
    page_size_query_param = 'pagesize'
    # 指定分页时的最大页容量
    max_page_size = 5



class BookListView(APIView):


    def get(self,request):
        raise DatabaseError

        return Response({"message":"ok"})

    # 过滤后端设置
    filter_fields = ('bread', 'btitle', 'id')
    # 排序设置
    filter_backends = [OrderingFilter]
    # 指定排序字段
    ordering_fields = ('id', 'bread', 'bpub_date')

    # 关闭分页
    # pagination_class = None

    # 指定当前视图所使用的分页类
    pagination_class = StandardResultPagination


# list：获取一组数据的通用代码
# create：新增一个数据的通用代码
# retrieve：检索、获取，获取指定数据的通用代码
# update：修改指定数据的通用代码
# destroy：摧毁、删除，删除指定数据的通用代码
