from django.core.management.base import BaseCommand
import os
import requests

from django.conf import settings


class Command(BaseCommand):
    help = "Faz o download dos datasets do brasileirão"

    def add_arguments(self, parser):
        parser.add_argument("ano", nargs="+", type=str)

    def handle(self, *args, **options):
        ano = options["ano"].pop()
        r = requests.get(
            settings.DATASET_BRASILEIRAO.format(ano),
        )

        root_dir = os.getcwd()

        # A função os.path.join concatena os caminhos que são informados, com isso não precisamos nos
        # preocupar em montar corretamente o caminho do arquivo onde as informações serão salvas.
        with open(os.path.join(root_dir, "data", f"brasileirao-{ano}.json"), mode="w", encoding="utf-8") as f:
            f.write(r.text)

        self.stdout.write("Arquivo salvo com sucesso")
