from django.db import models


class Round(models.Model):
    id = models.BigIntegerField(primary_key=True, null=False)
    description = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = "tb_rounds"


class Club(models.Model):
    name = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = "tb_clubs"


class Match(models.Model):

    round = models.ForeignKey(Round, on_delete=models.SET_NULL, null=True)
    home_club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, related_name="home_club")
    away_club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, related_name="away_club")
    hour = models.TimeField()
    date = models.DateField()

    class Meta:
        db_table = "tb_matches"
