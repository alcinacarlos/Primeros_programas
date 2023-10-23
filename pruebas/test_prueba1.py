from prueba1 import numero_mayor
import pytest
@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
    (1, 1, 0),
    (0, 4, 4),
    (100, -100, 100),
    (-15, -1, -1),
    (-3, 8, 8),
    (9, 2, 9)
    ]
)
def test_numero_mayor_params(input_n1, input_n2, expected):
    assert numero_mayor(input_n1, input_n2) == expected