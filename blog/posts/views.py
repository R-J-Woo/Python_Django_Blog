from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Post
from .forms import WriteForm
# Create your views here.


class PostList(ListView):
    model = Post
    template_name = 'blogs/posts_list.html'


class PostWrite(FormView):
    template_name = 'blogs/post_write.html'
    form_class = WriteForm
    success_url = 'blogs/posts_list.html'


class PostDetail(DetailView):
    template_name = 'blogs/post_detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'
