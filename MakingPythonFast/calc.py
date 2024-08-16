import ctypes
import random

# Load the shared library into ctypes
calc_lib = ctypes.CDLL('./libcalc.so')

# Define a Python function that calls the Zig function
def calculate_pi_zig(n):
    return calc_lib.calculate_pi(n)

def calculate_pi_python(n):
    random.seed()

    counter = 0.0

    for _ in range(n):
        x = random.random()
        y = random.random()

        if x * x + y * y < 1.0:
            counter += 1.0

    return 4.0 * counter / n
