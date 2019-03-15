"""kiffert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, static
from django.urls import include,path
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls',namespace='home')),
    url(r'^reports/', include('apps.reports.urls', namespace='reports')),
    url(r'^account/', include('apps.account.urls', namespace='account')),
    url(r'^report-settings/', include('apps.report_settings.urls',namespace='report-settings'))
]