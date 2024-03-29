from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
import datetime

from .forms import RenovarDevolucaoLivro
from .models import Livro, CopiaLivro, Autor, OpiniaoUsuarioLivro


# function-based view
# Caso queiramos usar permissões em function-based views, importamos o decorator permission_required
# e aplicamos na function based view
# O decorator login_required serve pra limitar o acesso à view apenas aos usuários logados
# @login_required()
# @permission_required("catalogo.pode_marcar_copia_como_devolvida")
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
    request.session['ultimo_acesso'] = datetime.datetime.now().strftime(
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


@login_required
@permission_required("catalogo.pode_marcar_copia_como_devolvida", raise_exception=True)
def renovar_data_devolucao_livro(request, pk):

    copia = get_object_or_404(CopiaLivro, pk=pk)

    if request.method == "POST":
        form = RenovarDevolucaoLivro(request.POST)

        # o método is_valid() chama os validadores do form, tanto os padrões quanto os definidos pelo programador.
        # Se nenhuma exceção for gerada, esse método retorna True
        if form.is_valid():
            copia.devolucao = form.cleaned_data["nova_data_de_devolucao"]
            copia.save()

            return HttpResponseRedirect(reverse("catalogo:todas-as-copias-emprestadas"))

    else:
        nova_data_proposta = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenovarDevolucaoLivro(initial={"nova_data_de_devolucao": nova_data_proposta})

    context = {
        "form": form,
        "copia": copia
    }

    return render(request, "catalogo/renovar_data_devolucao_livro.html", context)


@login_required
def comentar_livro(request, pk):

    livro = get_object_or_404(Livro, pk=pk)

    if request.method == "POST":
        data = request.POST
        OpiniaoUsuarioLivro(
            usuario=request.user,
            livro=livro,
            comentario=data.get("comentario"),
            nota=data.get("nota")
        ).save()

        return HttpResponseRedirect(reverse("catalogo:detalhe-livro", args=(pk,)))

    else:
        context = {
            "livro": livro
        }

        return render(request, "catalogo/comentar_livro.html", context)


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


# Apenas usuário logados podem acessar essa view, por causa do mixin LoginRequiredMixin
class CopiasEmprestadasPorUsuarioListView(LoginRequiredMixin, generic.ListView):
    model = CopiaLivro
    template_name = 'catalogo/copias_emprestadas_por_usuario.html'
    paginate_by = 10

    # O método get_queryset é chamado quando os dados serão carregados do banco de dados
    # Por padrão, ele trás todos os registros, sem nenhum filtro
    def get_queryset(self):

        lista_copias = CopiaLivro.objects.filter(
            emprestado_para=self.request.user,
            status__exact='e'
        ).order_by('devolucao')

        return lista_copias


class TodasAsCopiasEmprestadasListView(PermissionRequiredMixin, generic.ListView):
    model = CopiaLivro
    template_name = 'catalogo/todas_as_copias_emprestadas.html'
    paginate_by = 10
    permission_required = ("catalogo.pode_marcar_copia_como_devolvida",)

    # O método get_queryset é chamado quando os dados serão carregados do banco de dados
    # Por padrão, ele trás todos os registros, sem nenhum filtro
    def get_queryset(self):

        lista_copias = CopiaLivro.objects.filter(
            status__exact='e'
        ).order_by('devolucao')

        return lista_copias
