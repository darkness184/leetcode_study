import pandas as pd
"""
The target of this function is to return the second highest salary from the Employee DataFrame. If there is no second highest salary, return null.

Condition:
- fillter the unique salaries
- sort the salaries in descending order

solution:
1. Drop duplicate salaries and sort the salaries in descending order:
    - Use the drop_duplicates() method to remove duplicate salary values.
    - Use the sort_values() method to sort the salaries in descending order.
2. Select the second highest salary:
    - the second highest salary must exist.
    - Otherwise, return none.

Note:
"""


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False, ignore_index=True)

    if len(sorted_salaries) >= 2:
        second_highest_salary = sorted_salaries.iloc[1]
    else:
        second_highest_salary = None
        
    return pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})
