use std::io;

fn main() {
    const STANDARD: i32 = 543;
    let mut num = String::new();
    io::stdin().read_line(&mut num).unwrap();
    let mut year = num.split_whitespace();
    let a: i32 = year.next().unwrap().parse().unwrap();
    println!("{}", a - STANDARD);
}
