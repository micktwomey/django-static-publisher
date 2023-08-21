from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from ...publish import publish


class Command(BaseCommand):
    help = "Statically publish your Django site"

    def handle(self, *args, **options):
        prefix = Path("/tmp/")
        publish(prefix)
        self.stdout.write(self.style.SUCCESS(f"Published to {prefix}"))
