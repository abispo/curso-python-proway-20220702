from django.core.management.base import BaseCommand

"""
    Sintaxe do comando: python manage.py download_data <ano>
    <ano> é o ano dos dados do brasileirao (2003 -> 2021)
    O arquivo deve ser salvo no diretório data como brasileirao-<ano>.json

"""

class Command(BaseCommand):
    pass
