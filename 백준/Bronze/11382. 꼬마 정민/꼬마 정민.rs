use std::io;

fn main() {
    let mut numbers = String::new();
    io::stdin().read_line(&mut numbers).unwrap();
    let nums: Vec<usize> = numbers
        .split_whitespace()
        .map(|x| -> usize { x.parse().unwrap() })
        .collect();
    println!("{}", nums[0] + nums[1] + nums[2]);
}
