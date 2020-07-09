import json

from django.http import JsonResponse, HttpResponse
from django.views import View

from booktest.models import BookInfo


class BookListView(View):
    '''获取'''

    def get(self, request):

        # 1.获取所有图书
        books = BookInfo.objects.all()

        # 整理格式
        book_li = []
        for book in books:
            book_li.append({
                "id": book.id,
                "btitle": book.btitle,
                "bpub_date": book.bpub_date,
                "bread": book.bread,
                "bcomment": book.bcomment})

        # 返回
        return JsonResponse(book_li, safe=False)

    def post(self, request):
        '''增加'''
        # 接收参数
        json_dict = json.loads(request.body.decode())
        btitle = json_dict.get("btitle")
        bpub_date = json_dict.get("bpub_date")

        # 校验

        # 保存到数据库
        book = BookInfo.objects.create(btitle=btitle, bpub_date=bpub_date)

        # 整理格式
        book_dict = {
            "id": book.id,
            "btitle": book.btitle,
            "bpub_date": book.bpub_date,
            "bread": book.bread,
            "bcomment": book.bcomment}

        # 返回
        return JsonResponse(book_dict, status=200)


class BookDetailView(View):

    def get(self, request, pk):

        # 获取一个对象
        try:
            book = BookInfo.objects.get(id=pk)
        except Exception as e:
            return JsonResponse({'detail': 'not found'}, status=404)

        # 整理格式
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment}

        return JsonResponse(book_dict)

    def put(self, request, pk):
        '''修改'''

        # 获取一个对象
        try:
            book = BookInfo.objects.get(id=pk)
        except Exception as e:
            return JsonResponse({'detail': 'not found'}, status=404)

        # 得到数据后修改数据
        json_dict = json.loads(request.body.decode())
        btitle = json_dict.get("btitle")
        bpub_date = json_dict.get("bpub_date")

        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()

        # 保存到数据库
        # BookInfo.objects.create(btitle=btitle,
        #                         bpub_date=bpub_date)

        # 整理格式
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment}

        return JsonResponse(book_dict)


    def delete(self,request,pk):
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



















