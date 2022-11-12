
from django.test import TestCase
from django.urls import reverse

from mensagens.models import Mensagem


class TestMensagemViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.mensagem_joe = Mensagem(
            titulo="Cachorro quente sabor chucrute", corpo="Sem comentários", autor="Joe"
        ).save()
        cls.mensagem_amanda = Mensagem(
            titulo="tri", corpo="sem texto", autor="Amanda"
        ).save()

    def test_view_index_disponivel_por_rota(self):
        response = self.client.get('/mensagens/')

        self.assertEqual(response.status_code, 200)

    def test_view_index_disponivel_por_rota(self):
        response = self.client.get(reverse('mensagens:index'))

        self.assertEqual(response.status_code, 200)

    def test_view_index_carrega_template_correto(self):
        response = self.client.get(reverse('mensagens:index'))

        self.assertTemplateUsed("mensagens/index.html")
        self.assertEqual(response.status_code, 200)
