In order to get the correct packages for this section, run
`pip install -r requirements.txt`.

## `pytest` options

Move into this directory and run `pytest`: you should see successes.

If you get `ImportError`s, try
```bash
export PYTHONPATH="${PYTHONPATH}:."
```
not the nicest thing, but for this simple section it'll do.

Break the code (e.g. change the +1 to -1) and verify that the tests break.

Run `pytest` with some options! Here are some useful ones:

- `pytest -k property` will run only tests with the word "property" in their name
- `pytest -m slow` will run only tests marked as "slow" with `@pytest.mark.slow` - we can use any word here!
- `pytest -m "not slow"` will only run tests that are _not_ marked as "slow"
- `pytest -v` will give information about every test being run
- `pytest --maxfail=1` will stop after the first failure (while the 
    default behavior is to keep going): try it while breaking the code!

- Marking a test with `@pytest.mark.skip` will skip it
- marking it with `@pytest.mark.xfail` will run it but "accept" the failure as expected
    (useful to see at a glance that everything else is still working, or to document 
    a known bug)

### Debugger usage

Often we need to access internal variables deep inside the code.
Let's simulate such a situation: in `code.py`, we have a `add_one_with_intermediate_values`
function with a variable `value_to_add`, which should equal 1.
Let's break the code by setting it to something else, like 
`int(np.exp(1j * np.pi).real)`.

Now, the test for it should fail:

```python
    def test_add_one_with_intermediate_values():
        input_value = 0
    
        result = add_one_with_intermediate_values(input_value)
    
>       assert result == 1
E       assert -1 == 1

test_debugger.py:8: AssertionError
```

Good, so we know that it is broken. But, the output depends 
on the `value_to_add` variable: how can we evaluate it?

One simple thing we can do is to run `pytest` with
`pytest --pdb`; this will drop us in a [PDB console](https://docs.python.org/3/library/pdb.html) 
as soon as an exception occurs:
```
test_debugger.py F
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> traceback >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def test_add_one_with_intermediate_values():
        input_value = 0
    
        result = add_one_with_intermediate_values(input_value)
    
>       assert result == 1
E       assert -1 == 1

test_debugger.py:8: AssertionError
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> entering PDB >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>> PDB post_mortem (IO-capturing turned off) >>>>>>>>>>>>>>>>>>>
> /home/jacopo/Documents/focc/testing/testing_basics/first_steps/test_debugger.py(8)test_add_one_with_intermediate_values()
-> assert result == 1
(Pdb) value_to_add
*** NameError: name 'value_to_add' is not defined
(Pdb) 
```

Often this might be what we need,
but in this case that's too late, since the variable `value_to_add`
is already out of scope. 

One alternative, which however requires us to modify the code slightly,
is to insert a `breakpoint()` command in the function's source code,
so that it reads

```python
def add_one_with_intermediate_values(number: int) -> int:
    value_to_add = int(np.exp(1j * np.pi).real)
    breakpoint()
    return number + value_to_add
```
Then, when we run `pytest` we'll get:

```python
$ pytest
...
test_debugger.py 
>>>>>>>>>>>>>>>>>>> PDB set_trace (IO-capturing turned off) >>>>>>>>>>>>>>>>>>>>
> /home/jacopo/Documents/focc/testing/testing_basics/first_steps/code.py(9)add_one_with_intermediate_values()
-> return number + value_to_add
(Pdb) value_to_add
-1
(Pdb) 
```

This is nice, and it solves our problem, but we can also do it in a way
which does not require us to modify the code. 

After removing the breakpoint, we can run 

```bash 
$ pytest -k intermediate --trace
```

which will run only tests with "intermediate" in their name; 
and it will drop us in a PDB console as soon as the test starts.

Then, we can move forward using the instruction `s` up to the point we care about:

```bash
============================= test session starts ==============================
platform linux -- Python 3.10.6, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/jacopo/Documents/focc/testing/testing_basics/first_steps, configfile: pytest.ini
plugins: hypothesis-6.59.0
collected 7 items / 6 deselected / 1 selected                                  

test_debugger.py 
>>>>>>>>>>>>>>>>>>>> PDB runcall (IO-capturing turned off) >>>>>>>>>>>>>>>>>>>>>
> /home/jacopo/Documents/focc/testing/testing_basics/first_steps/test_debugger.py(4)test_add_one_with_intermediate_values()
-> input_value = 0
(Pdb) s
> /home/jacopo/Documents/focc/testing/testing_basics/first_steps/test_debugger.py(6)test_add_one_with_intermediate_values()
-> result = add_one_with_intermediate_values(input_value)
(Pdb) s
--Call--
> /home/jacopo/Documents/focc/testing/testing_basics/first_steps/code.py(6)add_one_with_intermediate_values()
-> def add_one_with_intermediate_values(number: int) -> int:
(Pdb) s
> /home/jacopo/Documents/focc/testing/testing_basics/first_steps/code.py(7)add_one_with_intermediate_values()
-> value_to_add = int(np.exp(1j * np.pi).real)
(Pdb) s
> /home/jacopo/Documents/focc/testing/testing_basics/first_steps/code.py(9)add_one_with_intermediate_values()
-> return number + value_to_add
(Pdb) value_to_add
-1
(Pdb) 
```

These are really just to illustrate the possibilities we have, 
one may be more convenient than another in any given scenario.
The [documentation](https://docs.pytest.org/en/7.1.x/how-to/failures.html),
as always, has more details!