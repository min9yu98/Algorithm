use std::io;

fn main() {
    let mut s = String::new();
    io::stdin().read_line(&mut s);
    let mut name = s.trim();
    println!("{}{1}", name, "??!");
}
