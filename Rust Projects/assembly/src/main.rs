fn main() {

    println!("{} cars", production_rate_per_hour(1));
    println!("{} cars", production_rate_per_hour(3));
    println!("{} cars", production_rate_per_hour(5));
    println!("{} cars", production_rate_per_hour(6));
    println!("{} cars", production_rate_per_hour(7));
    println!("{} cars", production_rate_per_hour(9));
    println!("{} cars", production_rate_per_hour(10));
    println!("{} cars", working_items_per_minute(4));
    println!("{} cars", working_items_per_minute(0));
}

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