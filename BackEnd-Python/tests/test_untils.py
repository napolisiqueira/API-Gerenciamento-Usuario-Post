import pytest
from src.untils import eleva_quadrado

@pytest.mark.parametrize("text_input, expected", [(2, 4), (4, 16), (8, 64)])
def test_eleva_numero_ao_quadrado(text_input, expected):
  resultado = eleva_quadrado(text_input)
  assert resultado == expected

# @pytest.mark.parametrize("text_input, expected", [("", 4), (4, 16), (8, 64)])
def test_eleva_numero_ao_quadrado():
  # with pytest.raises(TypeError) as exc:
  resultado = eleva_quadrado("a")   
  assert resultado == "aa"