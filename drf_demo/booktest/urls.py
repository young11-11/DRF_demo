# 设置Django运行所依赖的环境变量
import os

if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_demo.settings')

# 让Django进行一次初始化
import django

django.setup()

from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^books/', views.BookListView.as_view()),

]

'''

from rest_framework.routers import SimpleRouter, DefaultRouter

# ① 创建Router对象
# router = SimpleRouter()
router = DefaultRouter()

# ② 注册视图集
router.register('books', views.BookInfoViewSet, basename='books')

# ③ 添加url配置
urlpatterns += router.urls

# 测试：打印生成的url配置项
for url in router.urls:
    print(url)
'''