import json

from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer


class BookListView(ListCreateAPIView):
    # 指定视图所使用的序列化器类
    serializer_class = BookInfoSerializer

    # 指定试图所使用的查询集
    queryset = BookInfo.objects.all()

    def get(self, request):
        """
        获取所有图书数据：
        ① 查询数据库获取所有的图书的数据
        ② 将所有图书的数据通过json进行返回
        """
        return self.list(request)

    def post(self, request):
        """
        新增一本图书数据：
        ① 获取参数并进行校验
        ② 创建图书对象并保存到数据库
        ③ 将新增图书数据通过json进行返回
        """
        return self.create(request)


class BookDetailView(RetrieveUpdateDestroyAPIView):
    # 指定视图所使用的序列化器类
    serializer_class = BookInfoSerializer

    # 指定视图所使用的查询集
    queryset = BookInfo.objects.all()

    def get(self, request, pk):
        """
        self.kwargs：字典，保存的是从url地址提取的所有的命名参数
        获取指定图书数据(根据pk)：
        ① 根据pk去数据库查询指定的图书数据
        ② 将图书数据通过json数据进行返回
        """
        return self.retrieve(request, pk)

    def put(self, request, pk):
        """
        修改指定图书数据(根据pk)：
        ① 根据pk去数据库查询指定的图书数据
        ② 获取参数并进行校验
        ③ 修改图书数据并保存到数据库
        ④ 将修改图书的数据通过json数据进行返回
        """
        return self.update(request, pk)

    def delete(self, request, pk):
        """
        删除指定图书数据(根据pk)：
        1. 根据pk去数据库查询指定的图书数据
        2. 删除指定图书数据
        3. 返回响应，status=204
        """
        return self.destroy(request, pk)

# list：获取一组数据的通用代码
# create：新增一个数据的通用代码
# retrieve：检索、获取，获取指定数据的通用代码
# update：修改指定数据的通用代码
# destroy：摧毁、删除，删除指定数据的通用代码
