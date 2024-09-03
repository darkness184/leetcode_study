import pandas as pd
"""
The target of this function is to return the nth highest salary from the Employee DataFrame. If there is no nth highest salary, return null.

Condition:
- The value of salary must be unique.
- The value of N must be positive and smaller than the number of unique salaries.

Solution:
1. Drop duplicate salaries and sort the salaries in descending order:
    - Use the drop_duplicates() method to remove duplicate salary values.
    - Use the sort_values() method to sort the salaries in descending order.
2. Select the nth highest salary:
    - the nth highest salary must exist (that mean: N > 0 and N <= number of unique salaries).
    - Otherwise, return none.

Note:
iloc[row_indexer, column_indexer]:
    row_indexer: Integer, list of integers, slice object, or boolean array specifying the rows to select.
    column_indexer: Integer, list of integers, slice object, or boolean array specifying the columns to select.
"""


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False, ignore_index=True)

    if len(sorted_salaries) >= N and N > 0:
        nth_salary = sorted_salaries.iloc[N-1]
        return pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})
    else:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})