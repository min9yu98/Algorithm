use std::cmp;
use std::io;

fn main() {
    let mut nums = String::new();
    io::stdin().read_line(&mut nums).unwrap();
    let num_array: Vec<&str> = nums.split_whitespace().collect();
    let x: i32 = num_array[0].parse().unwrap();
    let y: i32 = num_array[1].parse().unwrap();
    let z: i32 = num_array[2].parse().unwrap();

    if x - y == 0 && y - z == 0 {
        println!("{}", 10000 + x * 1000);
    } else if x - y != 0 && y - z != 0 && x - z == 0 {
        println!("{}", 1000 + x * 100);
    } else if x - y == 0 && y - z != 0 && x - z != 0 {
        println!("{}", 1000 + x * 100);
    } else if x - y != 0 && y - z == 0 && x - z != 0 {
        println!("{}", 1000 + y * 100);
    } else {
        let mut a = cmp::max(x, y);
        println!("{}", cmp::max(a, z) * 100);
    }
}
