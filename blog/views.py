from django.views.generic import ListView, DetailView

from .models import Post

class PublishPostsMixin(object):
    def get_queryset(self):
        return self.model.objects.live()

class PostListView(PublishPostsMixin, ListView):
    model = Post

class PostDetailView(PublishPostsMixin, DetailView):
    model = Post