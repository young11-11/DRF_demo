import json

from django.http import JsonResponse, HttpResponse, Http404
from django.views import View
from rest_framework.decorators import action
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

    # 指定路由Router生成url配置项时，从路径中提取参数的正则表达式
    lookup_value_regex = '\d+'

    @action(methods=['get'], detail=False)
    def latest(self, request):
        book = BookInfo.objects.latest('id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    @action(methods=['put'], detail=True)
    def read(self, request, pk):
        book = self.get_object()
        book.bread = request.data.get('read')
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)

# list：获取一组数据的通用代码
# create：新增一个数据的通用代码
# retrieve：检索、获取，获取指定数据的通用代码
# update：修改指定数据的通用代码
# destroy：摧毁、删除，删除指定数据的通用代码
