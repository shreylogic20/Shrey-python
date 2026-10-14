# THE TELEMETRY GAP CHECK

Beginner | data-processing

**Difficulty:** Easy
**Tags:** Data Processing

---

### Story

A Databricks ETL job needs to flag which columns have missing telemetry before any imputation or
modeling touches the table: the single most common first step in any real data pipeline.

---

### The Problem

No math here: count missing (`NA`) entries per column.

### Input Format

```
n k
col_1_name ... col_k_name
row_1 (k values, `NA` denotes missing)
...
row_n
```

### Output Format

`col_name missing_count`, one line per column, in the given column order.

### Constraints

- `1 <= n <= 10^5`, `1 <= k <= 100`
- Time limit: 1.0 second.

---

### Example

**Input**

```
4 2
a b
1 NA
NA NA
3 1
NA 2
```

**Output**

```
a 2
b 2
```
