import pandas as pd
"""
The tager of this function is to calculate the special bonus for the employees

condition:
- if the employee_id is even or the name starts with 'M', the bonus is 0
- otherwise, the bonus is equal to the salary
solution:
1. calculate the bonus based on the condition
2. sort the employees by employee_id in ascending order
3. return the employee_id and bonus columns

note:
- using `apply()` to apply a function along the axis of the DataFrame
`.apply(func, axis=0, raw=False, result_type=None, args=(), **kwds)`
**func**: function - Function to apply to each column or row.
**axis**: {0 or ‘index’, 1 or ‘columns’}, default 0 - Axis along which the function is applied:
    - 0 or ‘index’: apply function to each column.
    - 1 or ‘columns’: apply function to each row.
**raw**: bool, default False - Determines if the function should be applied to the raw values or the index labels.
**result_type**: {‘expand’, ‘reduce’, ‘broadcast’, None}, default None - These only act when axis=1 (columns):
    - ‘expand’: list-like results will be turned into columns.
    - ‘reduce’: returns a Series if possible rather than expanding list-like results. This is the opposite of ‘expand’.
    - ‘broadcast’: results will be broadcast to the original shape of the frame, the original index and columns will be retained.
    - The default behaviour (None) depends on the return value of the applied function: list-like results will be expanded (returning DataFrame).
**args**: tuple - Positional arguments to pass to func in addition to the array/series.
**kwds**: dict - Additional keyword arguments to pass as keywords arguments to func.
"""


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(
        lambda col: col['salary'] * 0 \
            if ((col['employee_id'] % 2 == 0) | (col['name'].startswith("M")))
            else col['salary'], axis=1
    )
    employees.sort_values(by='employee_id', 
                          ascending=True, 
                          ignore_index=True, 
                          inplace=True)
    return employees[['employee_id', 'bonus']]