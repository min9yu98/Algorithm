use std::cmp;
use std::io;

fn main() {
    let mut x = String::new();
    io::stdin().read_line(&mut x).unwrap();
    let num_array: Vec<&str> = x.split_whitespace().collect();
    let num: i32 = num_array[0].parse().unwrap();
    for i in 1..10 {
        println!("{} * {} = {}", num, i, num * i);
    }
}
