import numpy as np

def add_one(number: int) -> int:
    return number + 1

def add_one_with_intermediate_values(number: int) -> int:
    value_to_add = int(-np.exp(1j * np.pi).real)
    
    return number + value_to_add