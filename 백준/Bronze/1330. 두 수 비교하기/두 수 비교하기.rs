use std::io;

fn main() {
    let mut numbers = String::new();
    io::stdin().read_line(&mut numbers).unwrap();
    let num_array: Vec<&str> = numbers.split_whitespace().collect();
    let first = num_array[0].parse::<i32>().unwrap();
    let second = num_array[1].parse::<i32>().unwrap();

    if first > second {
        println!(">");
    } else if first < second {
        println!("<");
    } else {
        println!("==");
    }
}
