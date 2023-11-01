use std::io;

fn main() {
    let mut num_array = String::new();
    io::stdin().read_line(&mut num_array).unwrap();
    let numbers: Vec<&str> = num_array.split_whitespace().collect();
    let number_first = numbers[0].parse::<i32>().unwrap();
    let number_second = numbers[1].parse::<i32>().unwrap();
    println!("{}", number_first - number_second);
}
