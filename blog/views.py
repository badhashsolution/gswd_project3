from django.shortcuts import render

from .models import Post

def blog_list(request, *args, **kwargs):
    post_list = Post.objects.filter(published=True)
    template_name = "post_list.html"

    context = {
        "post_list": post_list
    }
    return render(request, template_name, context)
