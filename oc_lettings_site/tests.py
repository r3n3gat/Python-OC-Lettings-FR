"""
Tests for oc_lettings_site app (home + error pages).
"""

from django.test import TestCase, override_settings
from django.urls import include, path, reverse

from oc_lettings_site import views


def trigger_500(_request):
    """Raise an error intentionally to trigger the 500 handler."""
    raise RuntimeError("Intentional error for testing 500 handler.")


# IMPORTANT:
# When ROOT_URLCONF points to this module, Django expects `urlpatterns`.
# We also include lettings/profiles here so template namespaces exist.
urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include(("lettings.urls", "lettings"), namespace="lettings")),
    path("profiles/", include(("profiles.urls", "profiles"), namespace="profiles")),
    path("trigger-500/", trigger_500, name="trigger_500"),
]


class OCLettingsSiteViewsTests(TestCase):
    """Integration tests for home and custom error pages."""

    def test_index_status_code_and_templates(self) -> None:
        url = reverse("index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertTemplateUsed(response, "base.html")

    @override_settings(DEBUG=False, ALLOWED_HOSTS=["testserver"])
    def test_custom_404_template_used(self) -> None:
        response = self.client.get("/does-not-exist/")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    @override_settings(
        DEBUG=False,
        ALLOWED_HOSTS=["testserver"],
        ROOT_URLCONF="oc_lettings_site.tests",
    )
    def test_custom_500_template_used(self) -> None:
        self.client.raise_request_exception = False
        response = self.client.get("/trigger-500/")
        self.assertEqual(response.status_code, 500)
        self.assertTemplateUsed(response, "500.html")
