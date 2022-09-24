import os
import sys

from django.core.management.base import BaseCommand
import requests

from core.models import Round, Club, Match


class Command(BaseCommand):
    help = "Salva no banco de dados as informações nos datasets baixados"

    def add_arguments(self, parser):
        parser.add_argument("ano", nargs="+", type=str)

    def handle(self, *args, **options):

        ano = options["ano"].pop()
        filepath = os.path.join(os.getcwd(), "data", f"brasileirao-{ano}.json")

        try:
            with open(filepath, mode="r", encoding="utf-8"):
                pass

        except FileNotFoundError:
            self.stdout.write(f"O {filepath} não existe")
            sys.exit(-1)
