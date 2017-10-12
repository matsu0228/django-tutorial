from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/report', views.export_csv, name='export_csv'),
    url(r'^post/debug_pdf', views.debug_pdf, name='debug_pdf'),
    url(r'^post/pdf', views.export_pdf, name='export_pdf'),
    # url(r'^post/proxy_plot', views.proxy_plot, name='proxy_plot'),
]
