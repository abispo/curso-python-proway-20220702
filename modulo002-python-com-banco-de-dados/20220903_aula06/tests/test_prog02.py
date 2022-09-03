import unittest
from unittest.mock import MagicMock, patch

from prog02 import retorna_info_criptomoeda


class TestProg02(unittest.TestCase):

    @patch("prog02.requests")
    def test_retorna_info_criptomoeda_deve_retornar_informacoes_da_criptomoeda(self, mock_requests):

        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "data": {
                "id": "bitcoin",
                "rank": "1",
                "symbol": "BTC",
                "name": "Bitcoin",
                "supply": "19140231.0000000000000000",
                "maxSupply": "21000000.0000000000000000",
                "marketCapUsd": "377457880688.2398024946493442",
                "volumeUsd24Hr": "7029873152.7398106816986864",
                "priceUsd": "19720.6544000560809582",
                "changePercent24Hr": "-0.9182325388191735",
                "vwap24Hr": "19867.7572029255987171",
                "explorer": "https://blockchain.info/"
                },
            "timestamp": 1662234834952
        }

        mock_requests.get.return_value = mock_response


        # Act
        resultado = retorna_info_criptomoeda("bitcoin")

        # Assert
        self.assertEqual("Bitcoin", resultado["nome"])
        self.assertEqual("BTC", resultado["simbolo"])
        self.assertEqual("19720.65", resultado["preco"])
        self.assertEqual("7029873152.74", resultado["volume24h"])

        mock_requests.get.assert_called_once_with("https://api.coincap.io/v2/assets/bitcoin")
        mock_response.json.assert_called_once()
