from django.test import TestCase

from mensagens.models import Mensagem


class TestMensagem(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.postit = Mensagem(titulo="Cachorro quente sabor chucrute", corpo="Sem comentários", autor="Joe").save()

    def test_slug_titulo_deve_retornar_titulo_slugificado(self):

        mensagem = Mensagem.objects.first()

        self.assertEqual(
            mensagem.slug_titulo(), 'cachorro-quente-sabor-chucrute'
        )
