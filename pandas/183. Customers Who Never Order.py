import pandas as pd
"""
The target of this function is to return the customers who never order anything

condition: id_orders should be null after merging the customers and orders dataframes with key present for customers
solution:
1. merge the customers and orders dataframes with key present for customers
2. filter the rows that have id_orders as null
3. rename the column name to Customers
4. return the Customers column

note:
- using `merge()` to merge the customers and orders dataframes
**how**: {‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘inner’ - Type of merge to be performed.
    - left: use only keys from left frame, similar to a SQL left outer join; preserve key order.
    - right: use only keys from right frame, similar to a SQL right outer join; preserve key order.
    - outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically.
    - inner: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys.
**on**: label or list - Column or index level names to join on. These must be found in both DataFrames. If `on` is None and not merging on indexes then this defaults to the intersection of the columns in both DataFrames.
**left_on**: label or list, or array-like - Column or index level names to join on in the left DataFrame. Can also be an array or list of arrays of the length of the left DataFrame. These arrays are treated as if they are columns.
**right_on**: label or list, or array-like - Column or index level names to join on in the right DataFrame. Can also be an array or list of arrays of the length of the right DataFrame. These arrays are treated as if they are columns.
**suffixes**: tuple of (str, str), default (‘_x’, ‘_y’) - Suffix to apply to overlapping column names in the left and right side, respectively.
**indicator**: bool or str, default False - If True, adds a column to output DataFrame called “_merge” with information on the source of each row.
**validate**: str, optional - If specified, checks if merge is of specified type.
**errors**: str, default ‘raise’ - If ‘raise’, raises an exception if merge keys are not unique. If ‘ignore’, suppresses the error and returns all matches.
**sort**: bool, default False - Sort the join keys lexicographically in the result DataFrame. If False, the order of the join keys depends on the join type (how keyword).
**copy**: bool, default True - If False, avoid copy if possible.
"""


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df_merge = customers.merge(
        orders, 
        how='outer',
        left_on='id', 
        right_on='customerId',
        suffixes=('_customers', '_orders')
    )
    df_merge = df_merge[
        (df_merge['id_orders'].isnull())
    ]
    df_merge.rename(
        columns={'name': 'Customers'},
        inplace=True
    )
    return df_merge[['Customers']]
