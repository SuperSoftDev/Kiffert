from django.conf.urls import url
from django.views.generic import TemplateView
from apps.home.views import IndexView,LoginView,SignupView,LogoutView
app_name = 'home'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login', LoginView.as_view(), name='login'),
    url(r'^logout', LogoutView.as_view(), name='logout'),
    url(r'^signup', SignupView.as_view(), name='signup'),
]