from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = "Informações do projeto"

    def add_arguments(self, parser):
        parser.add_argument("message", nargs="+", type=str)

    def handle(self, *args, **options):
        message = options["message"]
        time = timezone.now().strftime("%d/%m/%Y %H:%M:%S")
        output = f"""
        Dados sobre o brasileirão 2003 - 2021
        {time}
        Mensagem: {message.pop()}
        """

        self.stdout.write(output)
