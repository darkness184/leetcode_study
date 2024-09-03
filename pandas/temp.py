import pandas as pd
"""
the target of this function is to return the employee with the highest salary in each department

condition:
- the employee with the highest salary in each department.

solution:
1. group the employees by departmentId and get the maximum salary for each department.
2. filter the employees with the maximum salary in each department.
3. merge the employees with the department dataframe to get name of the department.
4. drop the unnecessary columns.
5. rename the columns.
6. return the result dataframe.

note:
- using `groupby()` to group the employees by departmentId
- using `transform()` to get the maximum salary in each group of departmentID (using with group of dataframe or series)
    **max**: Return the maximum of the values for the requested axis.
- using `merge()` to merge the employees with the department dataframe
- using `drop()` to drop the unnecessary columns
- using `rename()` to rename the columns
"""


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    group_department = employee.groupby('departmentId')['salary'].transform('max')
    result_df = employee[employee['salary'] == group_department]
    result_df = result_df.merge(
        department,
        left_on='departmentId',
        right_on='id',
        how='left'
    )
    result_df = result_df.drop(columns=['id_x', 'id_y', 'departmentId'])
    result_df = result_df.rename(columns={'name_x': 'Employee', 
                                          'name_y': 'Department'})
    return result_df