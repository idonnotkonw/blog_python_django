from django.conf.urls import patterns, include, url
from django.contrib import admin
from work.views import login,add,index,register,logout
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',login),
    url(r'add/',add),
    url(r'index/(\d*)',index),
    url(r'register/',register),   
    url(r'logout/',logout),
)
