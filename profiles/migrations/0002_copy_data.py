"""
Data migration: copy Profile data from oc_lettings_site to profiles.
"""

from django.db import migrations


def forwards_copy_data(apps, schema_editor):
    OldProfile = apps.get_model("oc_lettings_site", "Profile")
    Profile = apps.get_model("profiles", "Profile")

    for old_profile in OldProfile.objects.all():
        Profile.objects.create(
            id=old_profile.id,
            user_id=old_profile.user_id,
            favorite_city=old_profile.favorite_city,
        )


def backwards_delete_data(apps, schema_editor):
    Profile = apps.get_model("profiles", "Profile")
    Profile.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(forwards_copy_data, backwards_delete_data),
    ]
