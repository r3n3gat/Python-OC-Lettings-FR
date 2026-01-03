"""
Admin configuration for profiles models.
"""

from django.contrib import admin

from profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin view for Profile.
    """

    list_display = ("user", "favorite_city")
    search_fields = ("user__username", "favorite_city")
