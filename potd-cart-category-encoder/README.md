# CART CATEGORY ENCODER

Beginner | classical-ml | data-processing

**Difficulty:** Easy
**Tags:** Classic ML, Data Processing

---

### Story

Instacart's substitution-suggestion model needs the categorical product-department column encoded
before it can touch a single row of cart data. This is the same mechanic as the Airbnb amenity
question, different domain, because this exact operation shows up constantly across real pipelines.

---

### The Math

One-hot encode a categorical column into an `n x k` binary matrix, `k` the number of distinct
categories, columns alphabetical.

### Input Format

```
n
dept_1
...
dept_n
```

### Output Format

First line: distinct departments alphabetically. Next `n` lines: one-hot rows.

### Constraints

- `1 <= n <= 10^4`
- Time limit: 1.0 second.

---

### Example

**Input**

```
4
dairy
produce
dairy
bakery
```

**Output**

```
bakery dairy produce
0 1 0
0 0 1
0 1 0
1 0 0
```
