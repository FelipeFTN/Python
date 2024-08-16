# Building Zig
zig build-lib -dynamic calc.zig
mv libcalc.so libcalc_zig.so

# Building Rust
cargo build --release
mv target/release/libcalc.so libcalc_rust.so
