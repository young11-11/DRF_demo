import json

from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer


class BookListView(GenericAPIView):

    # 指定视图所使用的序列化器类
    serializer_class = BookInfoSerializer
    # 指定试图所使用的查询集
    queryset = BookInfo.objects.all()

    '''获取所有图书，增加图书'''

    def get(self, request):
        # 1.获取所有图书
        queryset = self.get_queryset()

        # 序列化所有数据
        serializer = self.get_serializer(queryset, many=True)

        # 返回
        return Response(serializer.data)

    def post(self, request):
        '''增加'''

        # 反序列化
        serializer = self.get_serializer(data=request.data)

        # 校验参数
        serializer.is_valid(raise_exception=True)

        # 保存到数据库
        serializer.save()

        # 返回
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)


class BookDetailView(GenericAPIView):

    # 指定视图所使用的序列化器类
    serializer_class = BookInfoSerializer

    # 指定视图所使用的查询集
    queryset = BookInfo.objects.all()

    def get(self, request, pk):

        # 获取一个对象
        instance = self.get_object()

        # 将图书数据进行序列化
        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    def put(self, request, pk):
        '''修改'''

        # 获取一个对象
        instance = self.get_object()

        # 反序列化-数据校验
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        # 反序列化-数据保存(save内部会调用序列化器类的update方法)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        '''获取要删除的对象'''
        instance = self.get_object()

        # 删除指定图书数据
        instance.delete()

        # 返回响应
        return Response(status=status.HTTP_204_NO_CONTENT)
