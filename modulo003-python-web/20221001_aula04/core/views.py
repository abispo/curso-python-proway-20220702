from django.shortcuts import render

from .models import Round


def index(request):

    all_rounds = Round.objects.values()

    years = []

    for round in all_rounds:
        years.append(round.get("year"))

    years = list(set(years))
    years.sort()

    return render(request, "core/index.html", {"years": years})
