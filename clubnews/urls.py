from django.urls import path
# from . import views
from .views import NewsView, NewsDetailView, AddNewsView, UpdateNewsView, DeleteNewsView # noqa


urlpatterns = [
    # path('', views.news, name='news'),
    path('clubnews/', NewsView.as_view(), name='clubnews'),
    path('article/<int:pk>', NewsDetailView.as_view(), name='newsdetail'),
    path('addnews/', AddNewsView.as_view(), name='addnews'),
    path('article/edit/<int:pk>', UpdateNewsView.as_view(), name='editnews'),
    path('article/delete/<int:pk>', DeleteNewsView.as_view(), name='deletenews'), # noqa
]
