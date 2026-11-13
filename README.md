# Simple Code Compare

A small side-by-side comparison of a simple task — **summing numbers in a vector/list/array using an explicit loop** — in four languages:

- Python
- C
- R
- Rust

## The Task

Sum the integers `[1, 2, 3, 4, 5]` using a loop (not the built-in `sum` functions).

## 1. Python

```python
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print(total)   # 15
```

**Key points**
- Dynamic typing, lists are heterogeneous by default.
- `for ... in` iterates directly over the values.
- Indentation defines the block (no braces).
- Very concise and readable.

## 2. C

```c
#include <stdio.h>

int main(void) {
    int numbers[] = {1, 2, 3, 4, 5};
    int n = 5;                 // must track length yourself
    int total = 0;

    for (int i = 0; i < n; i++) {
        total += numbers[i];
    }

    printf("%d\n", total);     // 15
    return 0;
}
```

**Key points**
- Static typing, fixed-size arrays (or you manage length yourself).
- Classic index-based `for` loop.
- Manual memory/size management.
- Braces `{}` and semicolons required.
- Lowest-level and most verbose of the four.

## 3. R

```r
numbers <- c(1, 2, 3, 4, 5)
total <- 0

for (num in numbers) {
  total <- total + num
}

print(total)   # 15
```

**Key points**
- Vector-oriented language; `c()` creates a vector.
- Assignment is usually `<-` (though `=` also works).
- `for (... in ...)` works, but R prefers vectorized operations (`sum(numbers)` is far more idiomatic).
- Braces optional for single statements, but commonly used.

## 4. Rust

```rust
fn main() {
    let numbers = vec![1, 2, 3, 4, 5];
    let mut total = 0;

    for num in &numbers {      // borrow to avoid moving
        total += num;
    }

    println!("{}", total);     // 15
}
```

**Key points**
- Strong static typing + ownership/borrowing system.
- `vec![]` creates a growable vector on the heap.
- `mut` is required to modify a variable.
- Iterating with `&numbers` (or `.iter()`) borrows the data safely.
- Extremely safe and performant, but has more ceremony than Python/R.

## Quick Syntax Comparison

| Feature              | Python          | C                     | R                | Rust                     |
|----------------------|-----------------|-----------------------|------------------|--------------------------|
| Container            | `list`          | C array               | vector (`c()`)   | `Vec<T>`                 |
| Loop style           | `for x in xs`   | index-based `for`     | `for x in xs`    | `for x in &xs`           |
| Mutable variable     | just assign     | normal                | normal           | must declare `mut`       |
| Type declaration     | none            | explicit              | none             | inferred or explicit     |
| Block delimiters     | indentation     | `{ }`                 | `{ }` (optional) | `{ }`                    |
| Safety / performance | high-level      | manual, fast          | high-level       | memory-safe + fast       |

---

Created for a quick language comparison.