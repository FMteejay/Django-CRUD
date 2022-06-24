from dataclasses import field
from pyexpat import model
from sre_constants import SUCCESS
from django.urls import reverse_lazy
from django.views import generic
from .models import Post 

class PostListView(generic.ListView):
    model = Post

from django.views import generic
from .models import Post

class PostCreateView(generic.CreateView):
    model = Post
    fields = {
        "__all__"
    }
    success_url = reverse_lazy("blog:all")

from django.views import generic
from .models import Post

class PostDetailView(generic.DetailView):
    model = Post

from django.views import generic
from .models import Post 

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = {
        "__all__"
    }
    success_url: reverse_lazy("blog.all")

from django.views import generic
from .models import Post

class PostDeleteView(generic.Delete.View):
    model = Post
    field = {
        "__all__"
    }
    success_url: reverse_lazy("blog,all")