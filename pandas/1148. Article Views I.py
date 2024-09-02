import pandas as pd
"""
The taget of this function is to return the author_id of the articles that have been viewed by their own author

condition: author_id should be equal to viewer_id
solution:
1. filter the rows that have author_id equal to viewer_id
2. return the author_id of the filtered rows
3. sort the author_id in ascending order and drop the duplicates

note:
- using `sort_values()` to sort the value of column author_id in ascending order
**by**: str or list of str - The column(s) to sort by. Required parameter.
**axis**: {0 or ‘index’, 1 or ‘columns’}, default 0 - The axis to sort along. 0 or ‘index’ to sort rows, 1 or ‘columns’ to sort columns.
**ascending**: bool or list of bool, default True - Sort ascending vs. descending. When the `by` parameter is a list, `ascending` can be a list of booleans to specify the sort order for each column.
**inplace**: bool, default False - If True, perform operation in-place.
**kind**: {‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, default ‘quicksort’ - Choice of sorting algorithm.
**na_position**: {‘first’, ‘last’}, default ‘last’ - Puts NaNs at the beginning if ‘first’; puts NaNs at the end if ‘last’.
**ignore_index**: bool, default False - If True, the resulting axis will be labeled 0, 1, …, n - 1.
**key**: callable, optional - Apply the key function to the values before sorting.

- using `drop_duplicates()` to drop the duplicates in the column author_id
**subset**: column label or sequence of labels, optional - Specifies which columns to consider for identifying duplicates.
**keep**: {‘first’, ‘last’, ’False’}, default ‘first’ - Determines which duplicates (if any) to keep: ‘first’ keeps the first occurrence, ‘last’ keeps the last occurrence, and False drops all duplicates.
**inplace**: bool, default False - If True, performs the operation in-place and modifies the original DataFrame.
**ignore_index**: bool, default False - If True, the resulting DataFrame will have a new index from 0 to n-1.
==> After using `drop_duplicates()` the index still reamins the same, so we need to reset the index using `reset_index()` or parameter `ignore_index=True`.
"""


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[
        (views['author_id'] == views['viewer_id'])
    ]
    df.rename(
        columns={'author_id': 'id'},
        inplace=True
    )
    df_fillter = df[['id']].drop_duplicates()
    df_fillter = df_fillter.sort_values(by='id', ascending=True, ignore_index=True)
    return df_fillter[['id']]