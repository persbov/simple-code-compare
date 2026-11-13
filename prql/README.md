# PRQL vs SQL – Simple Sum Example

**High-level algorithm (same in both):**
1. Start from a table of numbers
2. Add all the values together
3. Show the total

---

### PRQL version (`sum_list.prql`)

```prql
from numbers
aggregate {
  total = sum value
}
```

---

### Classic SQL version (`sum_list.sql`)

```sql
SELECT SUM(value) AS total
FROM numbers;
```

---

### Quick comparison

| Aspect              | PRQL                              | SQL                          |
|---------------------|-----------------------------------|------------------------------|
| Style               | Pipeline (step by step)           | Nested / declarative         |
| Readability         | Usually clearer for complex queries | Can become hard to read     |
| Modern features     | Variables, functions, cleaner syntax | Limited                      |
| Compatibility       | Compiles to SQL                   | Runs directly                |
| Age                 | New (modern alternative)          | 50+ years old                |

PRQL is designed to be a cleaner, more modern way to write the same kind of queries that SQL does.
