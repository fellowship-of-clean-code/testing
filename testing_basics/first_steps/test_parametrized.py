import pytest

from code import add_one


@pytest.mark.parametrize(
    'in_value, out_value',
    [
        (0, 1),
        (100, 101),
        (-1, 0),
    ]
)
def test_function_adding_one_parametrized(in_value, out_value):
    assert add_one(in_value) == out_value