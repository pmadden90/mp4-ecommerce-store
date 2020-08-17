from django.shortcuts import render # noqa
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # noqa
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.
# def news(request):
#    return render(request, 'news.html', {})


class FixturesView(ListView):
    model = Post
    template_name = 'fixtures/fixtures.html'
    ordering = ['date']


class FixturesDetailView(DetailView):
    model = Post
    template_name = 'fixtures/fixturesdetails.html'


class AddFixturesView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'fixtures/addfixtures.html'
    # fields = '__all__'


class UpdateFixturesView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'fixtures/editfixtures.html'
    # fields = ('title', 'tab_title', 'body', 'category', 'header_image')


class DeleteFixturesView(DeleteView):
    model = Post
    template_name = 'fixtures/deletefixtures.html'
    success_url = reverse_lazy('fixtures')
    # fields = ('title', 'tab_title', 'body', 'category', 'header_image')
