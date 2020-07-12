from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^books/$', views.BookInfoViewSet.as_view({
        "get": "list",
        "post": "create"
    })),
    re_path(r'^books/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    })),
    re_path(r'^books/latest/$', views.BookInfoViewSet.as_view({
        "get": "latest",
    })),
    re_path(r'^books/(?P<pk>\d+)/read/$', views.BookInfoViewSet.as_view({
        "put": "read",
    }))
]
