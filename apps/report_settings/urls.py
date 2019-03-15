from django.conf.urls import url
from django.views.generic import TemplateView
from apps.report_settings.views import IndexView
app_name = 'report_settings'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]