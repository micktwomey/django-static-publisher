from pathlib import Path

from django.core.management.base import BaseCommand, CommandError, CommandParser

from ...publish import publish


class Command(BaseCommand):
    help = "Statically publish your Django site"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("destination", help="Folder to write to")

    def handle(self, *args, **options):
        prefix = Path(options["destination"])
        self.stdout.write(self.style.NOTICE(f"Writing to {prefix}"))
        for path in publish(prefix):
            self.stdout.write(f"Wrote to {path}")
        self.stdout.write(self.style.SUCCESS(f"Published to {prefix}"))
