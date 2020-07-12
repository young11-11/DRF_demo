import json

from django.http import JsonResponse, HttpResponse, Http404
from django.views import View
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer


class BookInfoViewSet(viewsets.ViewSet):

    def list(self, request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books,many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):

        try:
            book = BookInfo.objects.get(pk=pk)
        except  BookInfo.DoesNotExist:
            raise Http404

        serializer = BookInfoSerializer(book)
        return Response(serializer.data)

    def update(self, request, pk):

        try:
            book = BookInfo.objects.get(pk=pk)
        except  BookInfo.DoesNotExist:
            raise Http404

        serializer = BookInfoSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise Http404

        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

# list：获取一组数据的通用代码
# create：新增一个数据的通用代码
# retrieve：检索、获取，获取指定数据的通用代码
# update：修改指定数据的通用代码
# destroy：摧毁、删除，删除指定数据的通用代码
