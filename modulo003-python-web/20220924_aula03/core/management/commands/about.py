from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = "Informações do projeto"

    def handle(self, *args, **options):
        time = timezone.now().strftime("%d/%m/%Y %H:%M:%S")
        output = f"""
        Dados sobre o brasileirão 2003 - 2021
        {time}
        """

        self.stdout.write(output)
