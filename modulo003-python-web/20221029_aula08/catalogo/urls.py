from django.urls import path
from . import views

app_name = "catalogo"

urlpatterns = [
    path("", views.index, name="index"),
    path("livros/", views.LivroListView.as_view(), name="lista-livros"),
    path("livros/<int:pk>/", views.LivroDetailView.as_view(), name="detalhe-livro"),
    path("livros/<uuid:pk>/renovar", views.renovar_data_devolucao_livro, name="renovar-data-devolucao-livro"),
    path("livros/<int:pk>/comentar", views.comentar_livro, name="comentar-livro"),
    path("autores/", views.AutorListView.as_view(), name="lista-autores"),
    path("autores/<int:pk>/", views.AutorDetailView.as_view(), name="detalhe-autor"),
    path("meus-emprestimos/", views.CopiasEmprestadasPorUsuarioListView.as_view(), name="meus-emprestimos"),
    path("todos-os-emprestimos/", views.TodasAsCopiasEmprestadasListView.as_view(), name="todas-as-copias-emprestadas")
]