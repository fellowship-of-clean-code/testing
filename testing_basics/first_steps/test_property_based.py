from hypothesis import given
from hypothesis import strategies as st
import pytest

from code import add_one

@given(st.integers())
@pytest.mark.slow
def test_function_adding_one_property_based(number):
    assert add_one(number) - number == 1