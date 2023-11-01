use std::io;

fn main() {
    let mut num_array = String::new();
    io::stdin().read_line(&mut num_array).unwrap();
    let numbers: Vec<&str> = num_array.split_whitespace().collect();
    let first: i32 = numbers[0].parse::<i32>().unwrap();
    let second: i32 = numbers[1].parse::<i32>().unwrap();
    let third: i32 = numbers[2].parse::<i32>().unwrap();
    println!("{}", (first + second) % third);
    println!("{}", ((first % third) + (second % third)) % third);
    println!("{}", (first * second) % third);
    println!("{}", ((first % third) * (second % third)) % third);
}
