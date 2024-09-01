import pandas as pd
"""
The target of this function is to fix the names of the users

condition:
- capitalize the first letter of the names
- sort the users by user_id in ascending order
solution:
1. capitalize the first letter of the names
2. sort the users by user_id in ascending order
3. return the users

note:
- using `str.capitalize()` to capitalize the first letter of the names
- using `sort_values()` to sort the users by user_id in ascending order
"""


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    users.sort_values(by='user_id',ascending=True, ignore_index=True, inplace=True)
    return users