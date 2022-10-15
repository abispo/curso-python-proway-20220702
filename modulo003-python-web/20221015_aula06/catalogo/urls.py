from django.urls import path
from . import views

app_name = "catalogo"

urlpatterns = [
    path("", views.index, name="index"),
    path("livros/", views.LivroListView.as_view(), name="lista-livros"),
    path("livros/<int:pk>", views.LivroDetailView.as_view(), name="detalhe-livro")
]