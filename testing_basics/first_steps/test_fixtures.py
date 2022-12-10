import pytest

from code import add_one

@pytest.fixture
def input_value():
   return 42

def test_function_adding_one_with_fixture(input_value):
    assert add_one(input_value) == 43