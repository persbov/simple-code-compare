// Simple sum of a list of numbers in Zig
// Algorithm: go through each number and add it to a running total

const std = @import("std");

pub fn main() void {
    const numbers = [_]i32{ 1, 2, 3, 4, 5 };
    var total: i32 = 0;

    for (numbers) |num| {
        total += num;
    }

    std.debug.print("Sum: {}\n", .{total}); // 15
}
