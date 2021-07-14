from csv import DictReader
from django.core.management.base import (
    BaseCommand,
    CommandError,
    )
from django.db import DatabaseError

from api.models import House


class Command(BaseCommand):
    help = 'Imports data about houses'

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='+')

    def handle(self, *args, **options):
        with open(options["file_path"][0]) as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                try:
                    House.objects.create(**row)
                except DatabaseError:
                    CommandError(f"Error processing row:\n{row}")

        self.stdout.write(self.style.SUCCESS('Import done'))
