from django.shortcuts import render # noqa
from django.views.generic import ListView, DetailView  # noqa
from .models import Post

# Create your views here.
# def news(request):
#    return render(request, 'news.html', {})


class NewsView(ListView):
    model = Post
    template_name = 'clubnews/clubnews.html'


class NewsDetailView(DetailView):
    model = Post
    template_name = 'clubnews/news_details.html'
