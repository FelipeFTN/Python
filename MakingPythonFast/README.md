# Python Performance with Zig

### Compile Zig dynamic library

```bash
zig build-lib -dynamic calc.zig
mv libcalc.so libcalc_zig.so
```

### Compile Rust dynamic library

```bash
cargo build --release
mv target/release/libcalc.so libcalc_rust.so
```

### Run Python

```bash
python3 main.py
```

### Results

```
$ python3 main.py
🐍 Python: 20.275019s
⚡ Zig:    2.271423s
🦀 Rust:   0.484555s
```
