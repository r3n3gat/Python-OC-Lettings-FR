"""
Database models for user profiles.
"""

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Profile model attached to a Django user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self) -> str:
        """
        Human-readable representation.

        Returns:
            Username.
        """
        return self.user.username
