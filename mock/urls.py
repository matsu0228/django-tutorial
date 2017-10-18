from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mock_main$', views.mock_main, name='mock_main'),
    url(r'^export_pdf$', views.export_pdf, name='export_pdf'),
    url(r'^test_form$', views.test_form, name='test_form'),
    url(r'^test_form_submit$', views.test_form_submit, name='test_form_submit'),
]
