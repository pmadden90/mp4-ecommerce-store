from django.urls import path
# from . import views
from .views import NewsView, NewsDetailView


urlpatterns = [
    # path('', views.news, name='news'),
    path('', NewsView.as_view(), name='clubnews'),
    path('article/<int:pk>', NewsDetailView.as_view(), name='newsdetail'),
]
