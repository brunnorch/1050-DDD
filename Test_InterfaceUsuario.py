from InterfaceUsuario import InterfaceUsuario


def test_solicitar_input_usuario():
    ddd = "71"
    result = ddd.isnumeric()

    assert result == True
