from django.shortcuts import render

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
