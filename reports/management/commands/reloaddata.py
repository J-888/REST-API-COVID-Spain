from django.core.management.base import BaseCommand, CommandError
from reports.models import Report

class Command(BaseCommand):
    help = 'Reloads the whole dataset'

    """def add_arguments(self, parser):
        parser.add_argument('url', nargs=1, type=int)"""

    def handle(self, *args, **options):
        Report.objects.all().delete()
