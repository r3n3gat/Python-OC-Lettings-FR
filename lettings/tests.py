"""
Tests for lettings app.
"""

from django.test import TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class LettingsViewsTests(TestCase):
    """
    Integration tests for lettings views and URLs.
    """

    @classmethod
    def setUpTestData(cls) -> None:
        address = Address.objects.create(
            number=1,
            street="Main Street",
            city="Paris",
            state="PA",
            zip_code=75000,
            country_iso_code="FRA",
        )
        cls.letting = Letting.objects.create(title="Nice flat", address=address)

    def test_lettings_index_status_code(self) -> None:
        url = reverse("lettings:lettings_index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_letting_detail_status_code(self) -> None:
        url = reverse("lettings:letting", kwargs={"letting_id": self.letting.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_letting_detail_404(self) -> None:
        url = reverse("lettings:letting", kwargs={"letting_id": 999999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class LettingsModelsTests(TestCase):
    """
    Unit tests for lettings models.
    """

    def test_address_str(self) -> None:
        address = Address(
            number=12,
            street="Rue de Python",
            city="Paris",
            state="PA",
            zip_code=75000,
            country_iso_code="FRA",
        )
        self.assertEqual(str(address), "12 Rue de Python")

    def test_letting_str(self) -> None:
        address = Address.objects.create(
            number=2,
            street="Another Street",
            city="Paris",
            state="PA",
            zip_code=75000,
            country_iso_code="FRA",
        )
        letting = Letting.objects.create(title="Test letting", address=address)
        self.assertEqual(str(letting), "Test letting")
