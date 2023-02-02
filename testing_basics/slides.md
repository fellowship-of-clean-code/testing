% The basics of testing
% Jacopo Tissino
% February 2nd, 2023

# Why test?

- Ensuring the code does what it is supposed to!
- Preventing changes from introducing regressions
- Encouraging modular and simple design

# What do I test for?

- Equivalent question to: how do I know my code isn't broken?
    - It's worthwhile (scientifically) to spend time in trying to answer it! 
- We will start with trivial examples, and then give ideas about how to test real code

# Why automate?

- Make it fast and easy to check whether anything's broken
- Allow other people to check their installation
- Can be made to run remotely within a pipeline

# How to automate?

- We could do it ourselves, but there's a better way!
- Testing frameworks available for all widely-used languages
- In python: __`pytest`__, `unittest`

