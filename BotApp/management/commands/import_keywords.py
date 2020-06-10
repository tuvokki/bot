import csv
from django.core.management import BaseCommand

from BotApp.models import IntentPointer, Intent


class Command(BaseCommand):
    help = 'Load a the intents and their keywords csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                if row[0].startswith('#'):
                    continue
                if not Intent.objects.filter(name=row[0]).exists():
                    intent = Intent.objects.create(
                        answer=row[0],
                        name=row[1]
                    )
                else:
                    intent = Intent.objects.get(name=row[0])

                for pointer in row[2].split('|'):
                    IntentPointer.objects.create(intent=intent, pointer=pointer)
