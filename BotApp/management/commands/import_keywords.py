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
                print(row)
                # pointer = IntentPointer.objects.create(
                #     # attr1=row[0]
                #     # attr2=row[1]
                # )