// This stub file contains items that aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]
pub fn production_rate_per_hour(speed: u8) -> f64 {
    const CARS: f64 = 221.0;
    if speed <= 4 {
        speed as f64 *CARS
    } else if speed <= 8 && speed >= 5 {
        (speed as f64 * CARS) * 0.90
    } else {
        (speed as f64 * CARS) * 0.77
    }
}
pub fn working_items_per_minute(speed: u8) -> u32 {
    const CARS: f64 = 221.0;
    const MINUTES: f64 = 60.0;
    let mut answer: f64 = 0.0;
    if speed <= 4 {
        answer = speed as f64 * CARS / MINUTES;
        return answer as u32
    } else if speed <= 8 && speed >= 5 {
        answer = (speed as f64 * CARS / MINUTES) * 0.90;
        return answer as u32
    } else {
        answer = (speed as f64 * CARS / MINUTES) * 0.77;
        return answer as u32
    }
}