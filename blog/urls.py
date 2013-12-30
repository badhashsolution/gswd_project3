from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.blog_list, name="list"),
    url(r"^(?P<pk>\d+)/$", views.blog_detail, name = "detail"),
)
