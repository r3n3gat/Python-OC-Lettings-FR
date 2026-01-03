"""
Admin configuration for lettings models.
"""

from django.contrib import admin

from lettings.models import Address, Letting


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """
    Admin view for Address.
    """

    list_display = ("number", "street", "city", "state", "zip_code", "country_iso_code")
    search_fields = ("street", "city", "state", "country_iso_code")


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    """
    Admin view for Letting.
    """

    list_display = ("title", "address")
    search_fields = ("title",)
