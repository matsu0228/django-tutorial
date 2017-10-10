from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dialogue/(?P<pk>[0-9]+)/$', views.dialogue_detail, name='dialog_detail'),
    url(r'^dialogue/new/$', views.dialogue_new, name='dialogue_new'),
    url(r'^dialogue/(?P<pk>\d+)/remove/$', views.dialogue_remove, name='dialogue_remove'),
]
