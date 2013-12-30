from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

class PublishPostsMixin(object):
    def get_queryset(self):
        queryset = super(PublishPostsMixin, self).get_queryset()
        return queryset.filter(published=True)

class PostListView(PublishPostsMixin, ListView):
    model = Post

class PostDetailView(PublishPostsMixin, DetailView):
    model = Post