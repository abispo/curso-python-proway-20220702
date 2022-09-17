from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:item_list_id>/detail", views.detail, name="detail")
]
