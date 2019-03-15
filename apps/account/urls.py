from django.conf.urls import url
from django.views.generic import TemplateView
from apps.account.views import IndexView
app_name = 'account'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]