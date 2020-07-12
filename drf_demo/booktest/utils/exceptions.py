# 注：DatabaseError是Django中所有数据库错误的父类
from django.db import DatabaseError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler



def exception_handler(exc, context):
    response = drf_exception_handler(exc, context)

    if response is None:
        # 补充数据库的异常处理
        if isinstance(exc, DatabaseError):
            response = Response({'detail': '数据库错误'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response