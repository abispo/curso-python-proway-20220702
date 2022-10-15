from django.http import HttpResponse
from django.shortcuts import render

from .models import Livro, CopiaLivro, Autor


def index(request):

    qtd_livros = Livro.objects.count()
    qtd_copias = CopiaLivro.objects.count()

    # filter -> WHERE
    qtd_copias_disponiveis = CopiaLivro.objects.filter(
        status__exact='d'
    ).count()

    qtd_autores = Autor.objects.count()

    context = {
        'qtd_livros': qtd_livros,
        'qtd_copias': qtd_copias,
        'qtd_copias_disponiveis': qtd_copias_disponiveis,
        'qtd_autores': qtd_autores
    }

    return render(request, 'catalogo/index.html', context=context)
