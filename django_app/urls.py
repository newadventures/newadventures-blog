from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
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
