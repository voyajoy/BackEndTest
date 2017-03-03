from django.core.management import BaseCommand

from sync_machine.models import Commit


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        Commit.data_loader.run()
        print('Task Complete.')
