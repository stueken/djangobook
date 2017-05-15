"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from . import views
from books import views as books_views

time_patterns = [
    url(r'^$', views.current_datetime),
    url(r'^plus/(\d{1,2})/$', views.hours_ahead),
]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', views.hello),
    url(r'^time/', include(time_patterns)),
    url(r'^search/$', books_views.search),
    url(r'^contact/$', views.contact),
]

if settings.DEBUG:
    urlpatterns += [url(r'^meta/$', views.display_meta), ]
