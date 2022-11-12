
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

    def test_view_nova_mensagem_metodo_get_deve_retornar_sucesso(self):
        response = self.client.get(reverse("mensagens:nova_mensagem"))

        self.assertTemplateUsed("mensagens/nova_mensagem.html")
        self.assertEqual(response.status_code, 200)

    def test_view_nova_mensagem_metodo_post_deve_salvar_nova_mensagem(self):
        response = self.client.post(
            reverse("mensagens:nova_mensagem"),
            {
                "mensagem_titulo": "A Linguagem de Programação Python",
                "mensagem_corpo": "Python é uma linguagem interpretada",
                "mensagem_autor": "Guido Von Rossum"
            }
        )

        mensagem = Mensagem.objects.filter(autor__startswith="Guido").first()

        self.assertEqual(mensagem.titulo, "A Linguagem de Programação Python")
        self.assertEqual(mensagem.corpo, "Python é uma linguagem interpretada")
        self.assertEqual(mensagem.autor, "Guido Von Rossum")

        self.assertEqual(response.status_code, 302)

    def test_view_nova_mensagem_metodo_post_deve_salvar_nova_mensagem_autor_anonimo(self):
        response = self.client.post(
            reverse("mensagens:nova_mensagem"),
            {
                "mensagem_titulo": "A Linguagem de Programação Python",
                "mensagem_corpo": "Python é uma linguagem interpretada",
                "mensagem_autor": ""
            }
        )

        mensagem = Mensagem.objects.filter(corpo__startswith="Python").first()

        self.assertEqual(mensagem.titulo, "A Linguagem de Programação Python")
        self.assertEqual(mensagem.corpo, "Python é uma linguagem interpretada")
        self.assertEqual(mensagem.autor, "Anônimo")

        self.assertEqual(response.status_code, 302)
