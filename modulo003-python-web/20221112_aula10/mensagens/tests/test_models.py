from django.test import TestCase

from mensagens.models import Mensagem


class TestMensagem(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.mensagem_joe = Mensagem(
            titulo="Cachorro quente sabor chucrute", corpo="Sem comentários", autor="Joe"
        ).save()
        cls.mensagem_amanda = Mensagem(
            titulo="tri", corpo="sem texto", autor="Amanda"
        ).save()

    def test_slug_titulo_deve_retornar_titulo_slugificado(self):

        mensagem = Mensagem.objects.first()

        self.assertEqual(
            mensagem.slug_titulo(), 'cachorro-quente-sabor-chucrute'
        )

    def test_str_model_deve_retornar_texto(self):
        mensagem = Mensagem.objects.filter(autor="Joe").first()

        self.assertEqual(
            str(mensagem), "Cachorro quente sabor chucrute"
        )

    def test_list_model_deve_retornar_texto(self):
        mensagem = Mensagem.objects.filter(autor="Joe")

        self.assertEqual(
            str(mensagem), "<QuerySet [Cachorro quente sabor chucrute]>"
        )

    def test_slug_titulo_deve_retornar_sem_slug(self):
        mensagem = Mensagem.objects.filter(autor="Amanda").first()

        self.assertEqual(
            mensagem.slug_titulo(), "sem-slug"
        )
