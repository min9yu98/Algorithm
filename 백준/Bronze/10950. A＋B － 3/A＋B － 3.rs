use std::cmp;
use std::io;

fn main() {
    let mut x = String::new();
    io::stdin().read_line(&mut x).unwrap();
    let x_array: Vec<&str> = x.split_whitespace().collect();
    let iter: i32 = x_array[0].parse().unwrap();
    for _ in 0..iter {
        let mut nums = String::new();
        io::stdin().read_line(&mut nums).unwrap();
        let nums: Vec<&str> = nums.split_whitespace().collect();
        let x: i32 = nums[0].parse().unwrap();
        let y: i32 = nums[1].parse().unwrap();
        println!("{}", x + y);
    }
}
