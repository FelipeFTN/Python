import timeit

number = 1000000

# Benchmark the Python function
python_time = timeit.timeit('calculate_pi_python(10)', setup='from calc import calculate_pi_python', number=number)

# Benchmark the Zig function
zig_time = timeit.timeit('calculate_pi_zig(10)', setup='from calc import calculate_pi_zig', number=number)

# Benchmark the Rust function
rust_time = timeit.timeit('calculate_pi_rust(10)', setup='from calc import calculate_pi_rust', number=number)

# Results
print(f'🐍 Python: {python_time:.6f}s')
print(f'⚡ Zig:    {zig_time:.6f}s')
print(f'🦀 Rust:   {rust_time:.6f}s')
