# A python project managed with poetry

This section deals with how to handle tests in a more complete python project,
which is managed with [`poetry`](https://python-poetry.org/).

## Setup

Start by [installing poetry with the official installer](https://python-poetry.org/docs#installing-with-the-official-installer).
You may verify that the installation was performed correctly by running
`poetry --version` on the command line; you should see version 1.3.1 (or more).

After this, you may enter a virtual environment created specifically 
for this project by running `poetry shell`; 
then, with `poetry install` you can install all the dependencies that 
were specified.

You can then run all commands within this virtual environment.

## How poetry works

The main file to look at here is `pyproject.toml`, which
determines the dependencies of the project; these are split into:

- Regular dependencies, under `[tool.poetry.dependencies]`:
    these are the ones which users of our software are expected to 
    need;
- development dependencies, under `[tool.poetry.group.dev.dependencies]`:
    these are the ones which we need while developing the software, 
    for example `pytest` to run the test suite, but which a user 
    should not need.

# Test Driven Development

The basic mantra is "red, green, refactor":

- __red__: write a test for the functionality we want to implement and run it:
    since the functionality is not implemented yet, it should fail (red);
- __green__: implement the functionality in as simple a way as possible, 
    writing the minimal code that will make the test pass;
- __refactor__: improve the code (structure, variable names, whatever), 
    relying on the test as a "safety net" to ensure we have not broken anything.

## Writing a sorting function

We want to write a simple function to sort a list.

### Red

We should then start with a test: we will write it like

```python
from my_project.sorting import sort_list

def test_sorting_inverted_list():
    
    data = [5, 4, 3, 2, 1]
    should_be_sorted = sort_list(data)
    
    assert should_be_sorted == [1, 2, 3, 4, 5]
```

We should insert it in a file in the `tests/` folder.
It is already there but commented out: uncomment it.

Running `pytest` should show a test failure:
right away, an `ImportError` will be raised 
since the function we are importing does not exist.

We can start by inserting a mock implementation, where 
we do not actually sort the list but return it unchanged.

```python
def sort_list(input_list: list) -> list:
    return input_list
```

Running the test now gives a _different_ error, as we would expect:
now the function is correctly imported, but the list we are returning
is not sorted, so we get

```python
collected 2 items                                                                                       

tests/test_module.py::test_myclass PASSED                                                         [ 50%]
tests/test_sorting.py::test_sorting_inverted_list FAILED                                          [100%]

=============================================== FAILURES ================================================
______________________________________ test_sorting_inverted_list _______________________________________

    def test_sorting_inverted_list():
    
        data = [5, 4, 3, 2, 1]
        should_be_sorted = sort_list(data)
    
>       assert should_be_sorted == [1, 2, 3, 4, 5]
E       assert [5, 4, 3, 2, 1] == [1, 2, 3, 4, 5]
E         At index 0 diff: 5 != 1
E         Full diff:
E         - [1, 2, 3, 4, 5]
E         + [5, 4, 3, 2, 1]

tests/test_sorting.py:8: AssertionError
======================================== short test summary info ========================================
FAILED tests/test_sorting.py::test_sorting_inverted_list - assert [5, 4, 3, 2, 1] == [1, 2, 3, 4, 5]
====================================== 1 failed, 1 passed in 0.09s ======================================

```

Remember that "error" here does not mean we are doing anything wrong!
This is the "red" step, so we _should_ have a test failure.

### Green

Now is the time to write the simplest possible code that'll make the test pass.
Here is a simple recursive implementation of merge-sort:

```python
def merge(list_1: list, list_2: list) -> list:
    result = []
    
    index_1 = 0
    index_2 = 0
    
    for _ in range(len(list_1)+len(list_2)):
        val_1 = list_1[index_1]
        val_2 = list_2[index_2]
        if val_1 <= val_2:
            result.append(val_1)
            index_1 += 1
        else:
            result.append(val_2)
            index_2 += 1

        if index_1 == len(list_1):
            result.extend(list_2)
            break
        if index_2 == len(list_2):
            result.extend(list_1)
            break
        
    return result

def sort_list(input_list: list) -> list:
    
    length = len(input_list)
    
    if length <= 1:
        return input_list

    return merge(
        sort_list(input_list[:length//2]), 
        sort_list(input_list[length//2:]), 
    )
```

### Refactor

I'll be cheeky here and say that the way to refactor this code is
to find out that there is a standard python function that 
does what we need better and faster:

```python
def sort_list(input_list: list) -> list:
    return sorted(input_list)
```
