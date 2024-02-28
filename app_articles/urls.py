from django.urls import path
from .views import (
    ArticleListsApiView,
    ArticlesCreateApiView,
    ArticlesRUDApiView,
    ArticleDetailApiView
)
urlpatterns = [
    path('list/articles/', ArticleListsApiView.as_view(),name='list-articles'),
    path('detail/articles/<int:pk>/', ArticleDetailApiView.as_view(),name='detail-articles'),
    # path('create/articles/', ArticlesCreateApiView.as_view(),name='create-articles'),
    # path('rud/articles/<int:pk>/', ArticlesRUDApiView.as_view(),name='rud-articles'),
]