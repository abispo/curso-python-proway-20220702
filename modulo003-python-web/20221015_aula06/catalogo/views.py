from django.shortcuts import render
from django.views import generic

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

    context = {
        'qtd_livros': qtd_livros,
        'qtd_copias': qtd_copias,
        'qtd_copias_disponiveis': qtd_copias_disponiveis,
        'qtd_autores': qtd_autores
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
