import pandas as pd
"""
The target of this function is to return the users with valid emails

condition:
- the email should end with '@leetcode.com' as domain
- the email should start with a letter
- the email should contain only letters (upper or lower case), digits, '.', '_', and '-'
solution:
1. filter the rows that have valid emails
2. return the filtered rows

note:
- using regex pattern to match the email
pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
PREFIX: ^[a-zA-Z][a-zA-Z0-9_.-]*
    ^: Asserts the position at the start of the string.
    [a-zA-Z]: Matches any single uppercase or lowercase letter. This ensures that the email prefix starts with a letter.
    [a-zA-Z0-9_.-]*: Matches zero or more characters that can be:
    a-z: Any lowercase letter.
    A-Z: Any uppercase letter.
    0-9: Any digit.
    _: An underscore.
    .: A period.
    -: A dash.
    *: This quantifier means "zero or more" of the preceding element. In this case, it means zero or more characters from the character class [a-zA-Z0-9_.-].
==> This part ensures that the email prefix can contain letters, digits, underscores, periods, and dashes.
DOMAIN: @leetcode\.com$
    @leetcode: Matches the literal @leetcode string.
    \.: Matches a literal period (.), escaping the dot to ensure it is treated as a literal character rather than a special regex character.
    com: Matches the literal com string.
    $: Asserts the position at the end of the string.
"""


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
    df = users[users['mail'].str.match(pattern)]
    return df