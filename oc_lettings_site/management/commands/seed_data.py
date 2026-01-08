from django.core.management.base import BaseCommand
from lettings.models import Address, Letting
from profiles.models import Profile
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Seed database with initial OC Lettings data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")

        # Clean existing data
        Letting.objects.all().delete()
        Address.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()

        addresses_data = [
            (3519, "Pheasant Ridge Road", "Birmingham", "AL", 35209, "USA"),
            (2972, "Fleming Way", "Montgomery", "AL", 36104, "USA"),
            (103, "Westport Drive", "Mobile", "AL", 36602, "USA"),
            (351, "Hill Haven Drive", "Huntsville", "AL", 35801, "USA"),
            (2341, "Hart Country Lane", "Tuscaloosa", "AL", 35401, "USA"),
            (123, "Lake Forest Drive", "Hoover", "AL", 35226, "USA"),
            (432, "Meadowbrook Road", "Dothan", "AL", 36301, "USA"),
            (876, "Pine Ridge Circle", "Auburn", "AL", 36830, "USA"),
            (1456, "Oakwood Avenue", "Decatur", "AL", 35601, "USA"),
            (789, "Willow Creek Road", "Madison", "AL", 35758, "USA"),
            (654, "Cedar Lane", "Florence", "AL", 35630, "USA"),
            (987, "Maple Street", "Gadsden", "AL", 35901, "USA"),
        ]

        lettings_titles = [
            "Joshua Tree Green Haus /w Hot Tub",
            "Oceanview Retreat",
            "Mountain Cabin Escape",
            "Urban Loft Downtown",
            "Sunny Beach House",
            "Cozy Lake Cottage",
            "Modern Farmhouse",
            "Luxury Penthouse",
            "Rustic Ranch",
            "Charming Bungalow",
            "Historic Villa",
            "Contemporary Studio",
        ]

        profiles_data = [
            ("Max", "max@example.com"),
            ("Clara", "clara@example.com"),
            ("John", "john@example.com"),
            ("Emma", "emma@example.com"),
            ("Lucas", "lucas@example.com"),
            ("Sophia", "sophia@example.com"),
            ("Liam", "liam@example.com"),
            ("Olivia", "olivia@example.com"),
            ("Noah", "noah@example.com"),
            ("Ava", "ava@example.com"),
            ("Ethan", "ethan@example.com"),
            ("Mia", "mia@example.com"),
        ]

        addresses = []
        for number, street, city, state, zip_code, country in addresses_data:
            addr = Address.objects.create(
                number=number,
                street=street,
                city=city,
                state=state,
                zip_code=zip_code,
                country_iso_code=country
            )
            addresses.append(addr)

        for title, addr in zip(lettings_titles, addresses):
            Letting.objects.create(title=title, address=addr)

        for username, email in profiles_data:
            user = User.objects.create(username=username, email=email)
            Profile.objects.create(user=user, favorite_city="Paris")

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
