import json

from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework import status
from rest_framework.views import APIView

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer


class BookListView(APIView):
    '''获取所有图书，增加图书'''

    def get(self, request):
        # 1.获取所有图书
        books = BookInfo.objects.all()

        # 序列化所有数据
        serializer = BookInfoSerializer(books,many=True)

        # 返回
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        '''增加'''

        # 反序列化
        serializer = BookInfoSerializer(data=request.data)

        # 校验参数
        serializer.is_valid(raise_exception=True)

        # 保存到数据库
        serializer.save()

        # 返回
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)


class BookDetailView(View):

    def get(self, request, pk):

        # 获取一个对象
        try:
            book = BookInfo.objects.get(id=pk)
        except Exception as e:
            return JsonResponse({'detail': 'not found'}, status=404)

        # 序列化成字典
        serializer = BookInfoSerializer(book)

        return JsonResponse(serializer.data)

    def put(self, request, pk):
        '''修改'''

        # 获取一个对象
        try:
            book = BookInfo.objects.get(id=pk)
        except Exception as e:
            return JsonResponse({'detail': 'not found'}, status=404)


        serializer = BookInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 反序列化-数据保存
        serializer.save()  # save内部调用序列化器类中的update方法
        return JsonResponse(serializer.data)


    def delete(self, request, pk):
        '''获取要删除的对象'''
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            # 图书不存在
            return JsonResponse({'detail': 'not found'}, status=404)

            # ② 删除指定图书数据
        book.delete()

        # ③ 返回响应
        return HttpResponse(status=204)
