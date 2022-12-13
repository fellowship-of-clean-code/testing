# Testing basics session

All exercises in this session are written in `python`,
using the `pytest` library.

Order of the exercises:

- `first_steps`
- `python_project`

## Types of tests / test ideas

Test types and examples/descriptions.

- Unit tests
    - Does this function yield the correct output for this input?
        Are the default values on this method working correctly?
- Regression tests
    - The code exits with an error when it receives a certain input.
        Before working on fixing the bug, I will write a test documenting 
        this behavior. This way, if the bug shows up again it will be caught.
- Integration tests
    - The data is processed in three steps in my code. Do I get the 
        correct output after all three?
- Trend tests
    - The output of the code should scale linearly with parameter $x$. Does it?
    - The gravitational force between two bodies should scale with the inverse
        square of their distance. 
- Special case tests
    - The gravitational force between two bodies should vanish when one of the masses
        is zero.
- End-to-end / validation tests
    - I trained a machine learning model. Is its validation score good enough?
- Exploratory tests
    - I need to use library $z$ for my project. As I learn its behavior,
        I will write tests that document my understanding of it.
        This way, besides formalizing the learning process, 
        I can quickly check whether the functionality that is useful to me
        has changed when a new version of that library is released.