
from django.contrib.auth.models import User
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
        User.objects.create_user(username="admin", password="123").save()


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

    def test_view_excluir_mensagem_com_sucesso(self):

        Mensagem(
            titulo="A linguagem PHP", corpo="PHP é ainda muito utilizado", autor="Jose"
        ).save()
        mensagem = Mensagem.objects.filter(corpo__startswith="PHP").first()
        self.client.login(username="admin", password="123")

        response = self.client.get(reverse("mensagens:excluir_mensagem", args=(mensagem.id,)))
        self.assertTemplateUsed("mensagens/mensagem_excluida.html")
        self.assertEqual(response.status_code, 200)

    def test_view_excluir_mensagem_erro_404(self):
        self.client.login(username="admin", password="123")
        response = self.client.get(reverse("mensagens:excluir_mensagem", args=(1000,)))

        self.assertEqual(response.status_code, 404)

    def test_view_excluir_mensagem_usuario_deslogado_deve_ser_redirecionado_para_o_login(self):
        response = self.client.get(reverse("mensagens:excluir_mensagem", args=(1000,)))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/mensagens/excluir-mensagem/1000/")
