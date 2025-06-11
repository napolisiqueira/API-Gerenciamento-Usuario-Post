import pytest
from pytest_mock import mocker
from src.untils import require_role
from src.untils import eleva_quadrado
from unittest.mock import patch
from http import HTTPStatus


@pytest.mark.parametrize("text_input, expected", [(2, 4), (0, 0), (1.5, 2.25)])
def test_eleva_numero_ao_quadrado_sucesso(text_input, expected):
    resultado = eleva_quadrado(text_input)
    assert resultado == expected


@pytest.mark.parametrize(
    "text_input, expected, msg",
    [
        (
            "a",
            TypeError,
            "unsupported operand type(s) for ** or pow(): 'str' and 'int'",
        ),
        (
            "None",
            TypeError,
            "unsupported operand type(s) for ** or pow(): 'str' and 'int'",
        ),
    ],
)
def test_eleva_numero_ao_quadrado_falha(text_input, expected, msg):
    with pytest.raises(expected) as exc:
        eleva_quadrado(text_input)
    assert str(exc.value) == msg


def test_require_role_sucesso(mocker):
    mock_user = mocker.Mock()
    mock_user.role.name = "admin"
    mocker.patch("src.untils.get_jwt_identity")
    mocker.patch("src.untils.db.get_or_404", return_value=mock_user)

    decorated_function = require_role("admin")(lambda: "success")
    result = decorated_function()
    assert result == "success"


def test_require_role_falha(mocker):
    mock_user = mocker.Mock()
    mock_user.role.name = "normal"
    mocker.patch("src.untils.get_jwt_identity")
    mocker.patch("src.untils.db.get_or_404", return_value=mock_user)

    
    decorated_function = require_role("admin")(lambda: "success")
    result = decorated_function()
    assert result == ({"message": "User dont have permission."},HTTPStatus.FORBIDDEN)
