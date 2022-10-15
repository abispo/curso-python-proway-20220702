from django.shortcuts import render
from django.views import generic
from datetime import datetime

from .models import Livro, CopiaLivro, Autor


# function-based view
def index(request):

    qtd_livros = Livro.objects.count()
    qtd_copias = CopiaLivro.objects.count()

    # filter -> WHERE
    qtd_copias_disponiveis = CopiaLivro.objects.filter(
        status__exact='d'
    ).count()

    qtd_autores = Autor.objects.count()
    qtd_visitas = request.session.get("qtd_visitas", 0)

    request.session['qtd_visitas'] = qtd_visitas + 1
    request.session['ultimo_acesso'] = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )

    context = {
        'qtd_livros': qtd_livros,
        'qtd_copias': qtd_copias,
        'qtd_copias_disponiveis': qtd_copias_disponiveis,
        'qtd_autores': qtd_autores,
        'qtd_visitas': qtd_visitas,
        'ultimo_acesso': request.session.get('ultimo_acesso')
    }

    return render(request, 'catalogo/index.html', context=context)


# class-based view
class LivroListView(generic.ListView):
    model = Livro
    context_object_name = "livro_list"
    paginate_by = 10

    def get_queryset(self):
        return Livro.objects.order_by("-id").all()


class LivroDetailView(generic.DetailView):
    model = Livro


class AutorListView(generic.ListView):
    model = Autor
    context_object_name = "autor_list"


class AutorDetailView(generic.DetailView):
    model = Autor
