
import unittest

from prog01 import inverte_texto


class TestProg01(unittest.TestCase):

    def test_inverte_texto_deve_retornar_texto_invertido(self):

        """
        Quando escrevemos um teste unitário, podemos dividir as fases do teste em 3:

        Preparo (Arrange)
            - Preparamos os dados que serão testados

        Chamada (Act)
            - Chamamos o trecho de código que será testado e pegamos o resultado

        Verificação (Assert)
            - Comparamos o resultado da chamada com o resultado que esperamos

        """

        # Arrange
        texto = "Python"
        saida_esperada = "nohtyP"

        # Act
        resultado = inverte_texto(texto)

        # Assert
        self.assertEqual(saida_esperada, resultado)

    def test_inverte_texto_deve_gerar_erro_se_a_entrada_nao_for_string(self):

        # Arrange (Preparação)
        texto = 20

        # Act
        with self.assertRaises(Exception) as exc_info:
            resultado = inverte_texto(texto)

        # Assert
        self.assertEqual(exc_info.exception.args[0], "Você deve passar um texto para a função")


if __name__ == "__main__":
    unittest.main()
