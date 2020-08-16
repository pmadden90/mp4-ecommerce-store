from django.shortcuts import render # noqa
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # noqa
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.
# def news(request):
#    return render(request, 'news.html', {})


class NewsView(ListView):
    model = Post
    template_name = 'clubnews/clubnews.html'
    ordering = ['-id']


class NewsDetailView(DetailView):
    model = Post
    template_name = 'clubnews/news_details.html'


class AddNewsView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'clubnews/addnews.html'
    # fields = '__all__'


class UpdateNewsView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'clubnews/editnews.html'
    # fields = ('title', 'tab_title', 'body', 'category', 'header_image')


class DeleteNewsView(DeleteView):
    model = Post
    template_name = 'clubnews/deletenews.html'
    success_url = reverse_lazy('clubnews')
    # fields = ('title', 'tab_title', 'body', 'category', 'header_image')
