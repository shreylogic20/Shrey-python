# THE BRIGHTNESS DIAL

Beginner | activation-functions

**Difficulty:** Easy
**Tags:** Activation Functions

---

### Story

Adobe's auto-brightness tool squashes an unbounded adjustment score into `(0, 1)` before applying it
as a blend factor: sigmoid, forward and backward, exactly as every deep learning framework
implements it.

---

### The Math

```
sigma(x)  = 1 / (1 + e^-x)
sigma'(x) = sigma(x) * (1 - sigma(x))
```

### Input Format

```
n
x_1 ... x_n
```

### Output Format

Two lines: `sigma(x)` and `sigma'(x)`, 6 decimals each.

### Constraints

- `1 <= n <= 10^5`, `|x_i| <= 50`
- Time limit: 1.0 second.

---

### Example

**Input**

```
1
0.5
```

**Output**

```
0.622459
0.235004
```
