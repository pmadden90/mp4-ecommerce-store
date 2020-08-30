from django.shortcuts import render # noqa
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # noqa
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.
# def news(request):
#    return render(request, 'news.html', {})


class AboutView(ListView):
    model = Post
    template_name = 'about/about.html'


class PitchesView(ListView):
    model = Post
    template_name = 'about/pitches.html'


class AddInfo(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'about/addnews.html'
    # fields = '__all__'


class EditAboutView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'about/editabout.html'
    # fields = ('title', 'tab_title', 'body', 'category', 'header_image')


class DeleteAboutView(DeleteView):
    model = Post
    template_name = 'about/deleteabout.html'
    success_url = reverse_lazy('about')
    # fields = ('title', 'tab_title', 'body', 'category', 'header_image')
