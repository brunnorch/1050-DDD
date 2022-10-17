from Destino import Destino
from DestinoRepository import DestinoRepository


def test_checa_se_ddd_existe():
    destino_repository = DestinoRepository()
    result = destino_repository.checa_se_ddd_existe(27)

    assert result == True

def test_adicionar_destino():
    destino_repository = DestinoRepository()
    rio_de_janeiro = Destino(21, "Rio de Janeiro")
    destino_repository.adicionar_destino(rio_de_janeiro)
    result = destino_repository.checa_se_cidade_existe(rio_de_janeiro.destino)

    assert result == True

def test_obter_destino_pelo_ddd():
    destino_repository = DestinoRepository()
    result = destino_repository.obter_destino_pelo_ddd(32)

    assert result == "Juiz de Fora"
