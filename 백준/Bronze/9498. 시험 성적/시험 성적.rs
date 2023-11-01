use std::io;

fn main() {
    let mut number = String::new();
    io::stdin().read_line(&mut number).unwrap();
    let numbers: Vec<&str> = number.split_whitespace().collect();
    let num: i32 = numbers[0].parse::<i32>().unwrap();
    if num >= 90 && num <= 100 {
        println!("A");
    } else if num >= 80 && num < 90 {
        println!("B");
    } else if num >= 70 && num < 80 {
        println!("C");
    } else if num >= 60 && num < 70 {
        println!("D");
    } else {
        println!("F");
    }
}
