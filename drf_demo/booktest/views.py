import json

from django.http import JsonResponse, HttpResponse, Http404
from django.views import View
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
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


class BookListView(ListAPIView):
    serializer_class = BookInfoSerializer
    queryset = BookInfo.objects.all()

    # 过滤后端设置
    filter_fields = ('bread', 'btitle', 'id')
    # 排序设置
    filter_backends = [OrderingFilter]
    # 指定排序字段
    ordering_fields = ('id', 'bread', 'bpub_date')

    # 关闭分页
    # pagination_class = None


# list：获取一组数据的通用代码
# create：新增一个数据的通用代码
# retrieve：检索、获取，获取指定数据的通用代码
# update：修改指定数据的通用代码
# destroy：摧毁、删除，删除指定数据的通用代码
