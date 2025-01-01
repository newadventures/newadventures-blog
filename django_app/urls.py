from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(
            url=staticfiles_storage.url("blog/favicon.ico"),
        ),
    ),
    path(f"{settings.ADMIN_PATH}/", admin.site.urls),
    path("", include("blog.urls", namespace="blog")),
]


"""
django-debug-toolbar for local development
see: https://django-debug-toolbar.readthedocs.io
"""
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
