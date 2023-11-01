use std::io;

fn main() {
    let mut numbers = String::new();
    io::stdin().read_line(&mut numbers).unwrap();
    let nums: Vec<&str> = numbers.split_whitespace().collect();
    let number = nums[0].parse::<i32>().unwrap();
    if (number % 4 == 0 && number % 100 != 0) || number % 400 == 0 {
        println!("1");
    } else {
        println!("0");
    }
}
