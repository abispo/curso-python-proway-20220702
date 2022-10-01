from django.db import models


class Round(models.Model):
    round_number = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    description = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.year} ({self.round_number})"

    class Meta:
        db_table = "tb_rounds"


class Club(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tb_clubs"


class Match(models.Model):

    round = models.ForeignKey(Round, on_delete=models.SET_NULL, null=True)
    home_club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, related_name="home_club")
    away_club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, related_name="away_club")
    home_goals = models.IntegerField(default=0)
    away_goals = models.IntegerField(default=0)
    stadium = models.CharField(max_length=100, null=True)
    hour = models.TimeField()
    date = models.DateField()

    class Meta:
        db_table = "tb_matches"
