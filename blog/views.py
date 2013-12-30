from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

def blog_list(request, *args, **kwargs):
    post_list = Post.objects.filter(published=True)
    template_name = "post_list.html"

    context = {
        "post_list": post_list
    }
    return render(request, template_name, context)

class PostListView(ListView):
    model = Post

    # WGG over-ride the query set on the class to get only published posts
    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        return queryset.filter(published=True)

def blog_detail(request, pk, *args, **kwargs):
    post = Post.objects.get(pk= pk, published=True)
    template_name = "blog/post_detail.html"

    context = {
        "post": post
    }

class PostDetailView(DetailView):
    model = Post
    def get_queryset(self):
        queryset = super(PostDetailView, self).get_queryset()
        return queryset.filter(published=True)
