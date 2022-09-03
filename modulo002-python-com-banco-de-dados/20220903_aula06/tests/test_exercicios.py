
import unittest

from exercicios import ex01


class TestExercicios(unittest.TestCase):

    def test_ex01_deve_ordenar_o_texto_em_ordem_alfabetica(self):

        # Arrange

        # Act

        # Assert
        self.assertEqual("abcelo", ex01("cebola"))
        self.assertEqual("aort", ex01("rato"))
        self.assertEqual("aaopst", ex01("sapato"))

    def test_ex01_deve_gerar_uma_excecao_se_a_entrada_nao_for_string(self):

        # Arrange
        mensagem_de_erro = "Você deve passar um tipo string para a função"

        # Act
        with self.assertRaises(Exception) as exc_info:
            ex01(325824)

        # Assert
        self.assertEqual(mensagem_de_erro, exc_info.exception.args[0])
