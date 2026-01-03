from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from oc_lettings_site import views

urlpatterns = [
    # Page d'accueil du site (utilisée par {% url 'index' %})
    path("", views.index, name="index"),

    # Apps
    path("lettings/", include(("lettings.urls", "lettings"), namespace="lettings")),
    path("profiles/", include(("profiles.urls", "profiles"), namespace="profiles")),

    # Admin
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    from oc_lettings_site.sentry_debug import trigger_error  # import local, uniquement en dev

    urlpatterns.append(
        path("sentry-debug/", trigger_error, name="sentry-debug"),
    )
