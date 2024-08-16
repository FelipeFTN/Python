use rand::prelude::*;

#[no_mangle]
pub extern "C" fn calculate_pi(n: i64) -> f64 {
    let mut rng = rand::thread_rng();
    let mut count = 0;

    for _ in 0..n {
        let x: f64 = rng.gen();
        let y: f64 = rng.gen();

        if x * x + y * y < 1.0 {
            count += 1;
        }
    }
    4.0 * count as f64 / n as f64
}
