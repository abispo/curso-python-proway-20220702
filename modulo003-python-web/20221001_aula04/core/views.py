from django.shortcuts import render

from .models import Round, Match


def index(request):

    all_rounds = Round.objects.values("year").distinct()
    years = [year_info.get("year") for year_info in all_rounds]
    years.sort()

    return render(request, "core/index.html", {"years": years})


def rounds_list(request, year):

    all_rounds = Round.objects.filter(year=year).order_by("round_number")

    return render(request, "core/rounds_list.html", {"all_rounds": all_rounds})


def round_detail(request, year, round_id):
    round = Round.objects.get(pk=round_id)
    all_matches = Match.objects.filter(round=round)

    return render(
        request,
        "core/round_detail.html", {"round": round, "all_matches": all_matches})

