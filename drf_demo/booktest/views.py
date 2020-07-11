import json

from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer


class MyListModelMixin:

    def list(self, request, *args, **kwargs):
        '''获取一组数据的通用代码'''

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class MyCreateModelMixin:

    def create(self, request, *args, **kwargs):
        """封装新增一个数据的通用代码"""

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)


class BookListView(MyListModelMixin,
                   MyCreateModelMixin,
                   GenericAPIView):
    # 指定视图所使用的序列化器类
    serializer_class = BookInfoSerializer

    # 指定试图所使用的查询集
    queryset = BookInfo.objects.all()

    def get(self, request):
        # 获取所有图书
        return self.list(request)

    def post(self, request):
        '''增加图书'''
        return self.create(request)


class MyRetrieveModelMixin:
    def retrieve(self, request, *args, **kwargs):
        """获取指定数据的通用代码"""

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class MyUpdateModelMixin:
    def update(self, request, *args, **kwargs):
        """修改指定数据的通用代码"""

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # 反序列化-数据保存(save内部会调用序列化器类的update方法)
        return Response(serializer.data)


class MyDestroyModelMixin:
    def destroy(self, request, *args, **kwargs):
        """删除指定数据的通用代码"""

        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookDetailView(MyRetrieveModelMixin,
                     MyUpdateModelMixin,
                     MyDestroyModelMixin,
                     GenericAPIView):
    # 指定视图所使用的序列化器类
    serializer_class = BookInfoSerializer

    # 指定视图所使用的查询集
    queryset = BookInfo.objects.all()

    def get(self, request, pk):
        '''获取一个对象'''
        return self.retrieve(request, pk)

    def put(self, request, pk):
        '''修改'''
        return self.update(request, pk)

    def delete(self, request, pk):
        '''获取要删除的对象'''
        return self.destroy(request, pk)

# list：获取一组数据的通用代码
# create：新增一个数据的通用代码
# retrieve：检索、获取，获取指定数据的通用代码
# update：修改指定数据的通用代码
# destroy：摧毁、删除，删除指定数据的通用代码
