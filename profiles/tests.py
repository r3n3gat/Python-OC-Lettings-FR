"""
Tests for profiles app.
"""

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from profiles.models import Profile


class ProfilesViewsTests(TestCase):
    """
    Integration tests for profiles views and URLs.
    """

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = User.objects.create(username="stevi")
        cls.profile = Profile.objects.create(user=cls.user, favorite_city="Paris")

    def test_profiles_index_status_code(self) -> None:
        url = reverse("profiles:profiles_index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_profile_detail_status_code(self) -> None:
        url = reverse("profiles:profile", kwargs={"username": self.user.username})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_profile_detail_404(self) -> None:
        url = reverse("profiles:profile", kwargs={"username": "does-not-exist"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class ProfilesModelsTests(TestCase):
    """
    Unit tests for profile model.
    """

    def test_profile_str(self) -> None:
        user = User.objects.create(username="user2")
        profile = Profile.objects.create(user=user, favorite_city="Lyon")
        self.assertEqual(str(profile), "user2")
