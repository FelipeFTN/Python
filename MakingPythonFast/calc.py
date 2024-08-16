import ctypes
import random

# Load the shared library into ctypes
calc_lib_zig = ctypes.CDLL('./libcalc_zig.so')
calc_lib_rust = ctypes.CDLL('./libcalc_rust.so')

# Define a Python function that calls the Zig function
def calculate_pi_zig(n):
    return calc_lib_zig.calculate_pi(n)

def calculate_pi_rust(n):
    return calc_lib_rust.calculate_pi(n)

def calculate_pi_python(n):
    random.seed()

    counter = 0.0

    for _ in range(n):
        x = random.random()
        y = random.random()

        if x * x + y * y < 1.0:
            counter += 1.0

    return 4.0 * counter / n
