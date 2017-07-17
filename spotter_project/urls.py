"""spotter_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ensure_csrf_cookie(TemplateView.as_view(template_name="index.html"))),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api/', include('workout.urls', namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns