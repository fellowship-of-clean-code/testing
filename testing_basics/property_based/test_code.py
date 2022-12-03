from hypothesis import given
from hypothesis import strategies as st

from code import add_one

@given(st.integers())
def test_function_adding_one_with_input_zero(number):
    assert add_one(number) - number == 1