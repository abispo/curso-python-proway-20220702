from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:year>/", views.rounds_list, name="rounds_list"),
    path("<int:year>/<int:round_id>", views.round_detail, name="round_detail")
]
