from django.core.management.base import BaseCommand
from apps.content.models import News
from tqdm import tqdm

class Command(BaseCommand):
    help = "sandbox command"

    def handle(self, *args, **options):
        pass