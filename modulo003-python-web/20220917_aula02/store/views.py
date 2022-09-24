from django.shortcuts import render, get_object_or_404
from .models import ItemsList


def index(request):

    all_items_list = ItemsList.objects.all()
    context = {"all_items_list": all_items_list}
    return render(request, "store/index.html", context)


def detail(request, item_list_id):

    items_list = get_object_or_404(ItemsList, pk=item_list_id)
    context = {"items_list": items_list}
    return render(request, "store/detail.html", context)
