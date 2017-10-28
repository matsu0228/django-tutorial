from django.conf.urls import url
from django.contrib.auth.views import login,logout

from . import views
# app_name = 'accounts'

urlpatterns = [
  url(r'^login/$', views.loginview, name="login"),
  url(r'^alert_settings/$', views.alert_settings, name="alert_settings"),
  # url(r'^login/$', login,
  #     {'template_name': 'accounts/login.html'},
  #     name='login'),
  url(r'^logout/$', logout, name='logout')
]
