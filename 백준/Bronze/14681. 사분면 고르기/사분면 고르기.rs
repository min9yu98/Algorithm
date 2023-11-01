use std::io;

fn main() {
    let mut x = String::new();
    let mut y = String::new();
    io::stdin().read_line(&mut x).unwrap();
    io::stdin().read_line(&mut y).unwrap();
    let num_x: i32 = x.trim().parse().unwrap();
    let num_y = y.trim().parse::<i32>().unwrap();
    if num_x > 0 && num_y > 0 {
        println!("1");
    } else if num_x > 0 && num_y < 0 {
        println!("4");
    } else if num_x < 0 && num_y < 0 {
        println!("3");
    } else if num_x < 0 && num_y > 0 {
        println!("2");
    }
}
