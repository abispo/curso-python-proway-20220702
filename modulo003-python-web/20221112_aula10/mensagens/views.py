from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Mensagem


def index(request):

    todas_mensagens = Mensagem.objects.all()
    context = {
        'todas_mensagens': todas_mensagens
    }

    return render(request, 'mensagens/index.html', context)


def nova_mensagem(request):

    if request.method == 'GET':
        return render(request, 'mensagens/nova_mensagem.html')

    if request.method == 'POST':

        post_data = request.POST

        titulo = post_data.get("mensagem_titulo")
        corpo = post_data.get("mensagem_corpo")
        autor = post_data.get("mensagem_autor").strip()

        if len(autor) == 0:
            autor = "Anônimo"

        Mensagem(titulo=titulo, corpo=corpo, autor=autor).save()

        return HttpResponseRedirect(reverse('mensagens:index'))


@login_required
def excluir_mensagem(request, pk):

    mensagem = get_object_or_404(Mensagem, pk=pk)
    mensagem.delete()

    return render(request, "mensagens/mensagem_excluida.html")
