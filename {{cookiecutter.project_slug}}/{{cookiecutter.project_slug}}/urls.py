"""{{ cookiecutter.project_slug }} URL Configuration."""
from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rotest/api/', include("rotest.api.urls")),
]
