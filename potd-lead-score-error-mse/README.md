# LEAD SCORE ERROR

Beginner | loss-functions

**Difficulty:** Easy
**Tags:** Loss Functions

---

### Story

A lead-scoring regressor is graded against actual conversion likelihood using the most standard
regression loss there is, but it has to match the framework reference exactly before it ships into
the training loop.

---

### The Math

```
MSE = (1/n) * sum_i (y_i - yhat_i)^2
```

### Input Format

```
n
y_1 yhat_1
...
y_n yhat_n
```

### Output Format

Scalar MSE, 6 decimals.

### Constraints

- `1 <= n <= 10^6`
- Time limit: 1.0 second.

---

### Example

**Input**

```
4
3 2.5
5 5
2.5 4
7 8
```

**Output**

```
0.875000
```
