from django.shortcuts import render

from .models import Round


def index(request):

    all_rounds = Round.objects.values("year").distinct()
    years = [year_info.get("year") for year_info in all_rounds]
    years.sort()

    return render(request, "core/index.html", {"years": years})
