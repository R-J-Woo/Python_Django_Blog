from xml.etree.ElementTree import Comment
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator

from users.decorators import login_required
from .models import Post, Comment
from .forms import WriteForm
# Create your views here.


@method_decorator(login_required, name='dispatch')
class PostList(ListView):
    model = Post
    template_name = 'blogs/posts_list.html'


@method_decorator(login_required, name='dispatch')
class PostWrite(FormView):
    template_name = 'blogs/post_write.html'
    form_class = WriteForm
    success_url = 'blogs/posts_list.html'


@method_decorator(login_required, name='dispatch')
class PostDetail(DetailView):
    template_name = 'blogs/post_detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'
