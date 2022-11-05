from django.test import TestCase

from mensagens.models import Mensagem


class TestMensagem(TestCase):

    def test_slug_titulo_deve_retornar_titulo_slugificado(self):
        postit = Mensagem(titulo="Cachorro quente sabor chucrute", corpo="Sem comentários", autor="Joe").save()

        self.assertEqual(
            postit.slug_titulo(), 'cachorro-quente-sabor-chucrute'
        )
