import pandas as pd
"""
The target of this function is to return the patients with Type I Diabetes

condition:
- In conditions column, the value should contain 'DIAB1'
- Data of conditions should be start with 'DIAB1'
solution:
1. Using regex pattern to match the conditions
2. filter the rows that have 'DIAB1' in the conditions
3. return the filtered rows

note:
- using regex pattern to match the conditions
pattern = r'\bDIAB1\w*'
\b: assert position at a word boundary
DIAB1: matches the characters DIAB1 literally (case sensitive)
\w*: matches any word character (equal to [a-zA-Z0-9_]) - between zero and unlimited times, as many times as possible, giving back as needed
==> This part ensures that the conditions contain the word DIAB1
"""


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    pattern = r'\bDIAB1\w*'
    df = patients[patients['conditions'].str.contains(pattern)]
    return df