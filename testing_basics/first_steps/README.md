Things to try:

Move into this directory and run `pytest`: you should see successes.

Break the code (e.g. change the +1 to -1) and verify that the tests break.

Run `pytest` with some options! Here are some useful ones:

- `pytest -k property` will run only tests with the word "property" in their name
- `pytest -m slow` will run only tests marked as "slow" with `@pytest.mark.slow` - we can use any word here!
- `pytest -m "not slow"` will only run tests that are _not_ marked as "slow"
- `pytest -v` will give information about every test being run

- marking a test with `@pytest.mark.skip` will skip it
- marking it with `@pytest.mark.xfail` will run it but "accept" the failure as expected
    (useful to see at a glance that everything else is still working, or to document 
    a known bug)
