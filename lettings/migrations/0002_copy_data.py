"""
Data migration: copy Address + Letting data from oc_lettings_site to lettings.
"""

from django.db import migrations


def forwards_copy_data(apps, schema_editor):
    OldAddress = apps.get_model("oc_lettings_site", "Address")
    OldLetting = apps.get_model("oc_lettings_site", "Letting")
    Address = apps.get_model("lettings", "Address")
    Letting = apps.get_model("lettings", "Letting")

    for old_address in OldAddress.objects.all():
        Address.objects.create(
            id=old_address.id,
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )

    for old_letting in OldLetting.objects.all():
        Letting.objects.create(
            id=old_letting.id,
            title=old_letting.title,
            address_id=old_letting.address_id,
        )


def backwards_delete_data(apps, schema_editor):
    Letting = apps.get_model("lettings", "Letting")
    Address = apps.get_model("lettings", "Address")
    Letting.objects.all().delete()
    Address.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("lettings", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(forwards_copy_data, backwards_delete_data),
    ]
