from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from blog.views import blog_list, blog_detail

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microblog.views.home', name='home'),
    # url(r'^microblog/', include('microblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', blog_list, name="blog_list"),
    url(r"^blog/(?P<pk>\d+)/$", blog_detail, name = "blog_detail"),


    url(r'^admin/', include(admin.site.urls)),

)
