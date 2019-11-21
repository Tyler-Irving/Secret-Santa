from django.core.management.base import BaseCommand, CommandError
from app import models

GROUP = [
    {"name": "Tyler Irving", "email": "tirving@basecampcodingacademy.org"},
    {"name": "Evil Tyler", "email": "eviletyler@gmail.com"},
]


class Command(BaseCommand):
    help = (
        "Seeds the database with dog products based on the dog store python benchmark"
    )

    def handle(self, *args, **options):
        for people in GROUP:
            self.create_people(people)

    def create_dog_product(self, people_data: dict):
        name = people_data.pop("name")
        movie, created = models.People.objects.get_or_create(
            name=name, defaults=people_data
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"{name} created"))
        else:
            self.stdout.write(f"{name} already exists")
