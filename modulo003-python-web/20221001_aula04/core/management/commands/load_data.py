import json
import os
import sys

from django.core.management.base import BaseCommand

from core.models import Round, Club, Match


class Command(BaseCommand):
    help = "Salva no banco de dados as informações nos datasets baixados"

    def add_arguments(self, parser):
        parser.add_argument("ano", nargs="+", type=str)

    def handle(self, *args, **options):

        ano = options["ano"].pop()
        filepath = os.path.join(os.getcwd(), "data", f"brasileirao-{ano}.json")

        try:
            with open(filepath, mode="r", encoding="utf-8") as _file:
                # json.load carrega o arquivo e já converte o seu conteúdo para um dicionário
                file_content = json.load(_file)

                # Pegamos as chaves desse dicionário que foi carregado
                round_keys = list(file_content.keys())

                for round_key in round_keys:
                    # Quebramos a string usando o "azinho" como separador, e pegamos sempre o número da rodada
                    round_id = int(round_key.split("\u00aa")[0])

                    # Se existir um registro na tabela tb_rounds com esse id, o método get_or_create retorna.
                    # Não não existir, ele cria o registro com esse ID e retorna o objeto
                    # _ serve pra receber o segundo valor da tupla. Usamos essa sintaxe quando queremos ignorar
                    # algum valor
                    round_obj, _ = Round.objects.get_or_create(round_number=round_id, year=int(ano))

                    # Salvamos um texto como descrição da rodada
                    round_obj.description = f"Rodada {round_id} de {ano}"
                    round_obj.save()

                    # Iterar sobre a lista de jogos
                    # file_content[round_key]
                    # Salvar informações sobre o clube
                    # Salvar informações sobre a partida

                    for match in file_content[round_key]:

                        home_club = match.get("clubs").get("home").upper().strip()
                        away_club = match.get("clubs").get("away").upper().strip()

                        home_club_obj, _ = Club.objects.get_or_create(name=home_club)
                        away_club_obj, _ = Club.objects.get_or_create(name=away_club)

                        match_hour = match.get("hour")

                        if len(match_hour) != 5:
                            match_hour = "00:00"

                        match_date = match.get("date")

                        match_date = match_date.split("/")
                        match_date = f"{match_date[2]}-{match_date[1]}-{match_date[0]}"

                        home_club_goals = match.get("goals").get("home")
                        away_club_goals = match.get("goals").get("away")

                        stadium = match.get("stadium").strip()

                        Match.objects.get_or_create(
                            round=round_obj,
                            home_club=home_club_obj,
                            away_club=away_club_obj,
                            home_goals=home_club_goals,
                            away_goals=away_club_goals,
                            stadium=stadium,
                            hour=match_hour,
                            date=match_date
                        )

        except FileNotFoundError:
            self.stdout.write(f"O arquivo {filepath} não existe.")
            sys.exit(-1)

        else:
            self.stdout.write(f"Arquivo {filepath} carregado com sucesso!")
