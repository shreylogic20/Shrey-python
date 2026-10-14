def count_missing_per_column(columns: list[str], rows: list[list[str]]) -> list[int]:
    """
    Count missing entries per column.

    columns: k column names, in order.
    rows: n rows, each a list of k raw string values. The exact literal
      string "NA" denotes missing; nothing else does ("N/A", "null" are
      real, non-missing values).

    Return a list of k counts, one per column, in the same order as
    `columns`, even when a count is 0.
    """
    # TODO: exact string equality against "NA", per column.
    count = [0] * len(columns)

    for row in rows:
        for i in range(len(columns)):
            if row[i] == "NA":

                count[i] += 1

    return count
