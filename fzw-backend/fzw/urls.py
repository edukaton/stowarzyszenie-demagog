"""fzw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import re

from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

api_urlpatterns = [
    path('', include('fzw.quizes.api.urls')),
]

urlpatterns = [
    path('api/v1/', include(api_urlpatterns)),
    path('admin/', admin.site.urls),
]


def _static(prefix, view=serve, **kwargs):
    return [
        re_path(
            r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), view,
            kwargs=kwargs),
    ]


if settings.MEDIA_ROOT:
    urlpatterns += _static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)

if not settings.DEBUG and settings.STATIC_ROOT:
    urlpatterns += _static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)
