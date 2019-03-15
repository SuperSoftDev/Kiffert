from django.conf.urls import url
from django.views.generic import TemplateView
from apps.reports.views import IndexView
app_name = 'reports'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]