import pandas as pd
"""
the target of this function is to return the tweet_id of tweets that have a content length greater than 15

condition: data of each row in col 'content' should be greater than 15
solution:
1. filter the rows that have content length greater than 15
    - use the str.len() method to get the length of each content
    - fillter row that have content length greater than 15
2. return the tweet_id of the filtered rows

note:
- using the `employees['name'].str` to access `pandas.core.strings.accessor.StringMethods` object, 
which allows you to perform vectorized string operations on the name column (like .len(), .consains(), .startswith(), etc)

- using `employees['name']` to access `pandas.Series` object.
"""

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[tweets['content'].str.len() > 15]
    return df[['tweet_id']]