fn main() {
    let numbers = vec![1, 2, 3, 4, 5];
    let mut total = 0;

    for num in &numbers {      // borrow to avoid moving
        total += num;
    }

    println!("{}", total);     // 15
}
