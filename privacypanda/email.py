"""
Code for identifying emails
"""
import re
from typing import List

import pandas as pd
from numpy import dtype as np_dtype

__all__ = ["check_emails"]

OBJECT_DTYPE = np_dtype("O")

# Whitelisted email suffix.
# TODO extend this
WHITELIST_EMAIL_SUFFIXES = [".co.uk", ".com", ".org", ".edu"]
EMAIL_SUFFIX_REGEX = "[" + r"|".join(WHITELIST_EMAIL_SUFFIXES) + "]"

# Simple email pattern
SIMPLE_EMAIL_PATTERN = re.compile(".*@.*" + EMAIL_SUFFIX_REGEX, re.I)


def check_emails(df: pd.DataFrame) -> List:
    """
    Check a dataframe for columns containing emails. Returns a list of column
    names which contain at least one emails

    "Emails" currently only concerns common emails, with one of the following
    suffixes: ".co.uk", ".com", ".org", ".edu"

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to check

    Returns
    -------
    List
        The names of columns which contain at least one email
    """
    private_cols = []

    for col in df:
        row = df[col]

        # Only check column if it may contain strings
        if row.dtype == OBJECT_DTYPE:
            for item in row:
                item = str(item)  # convert incase column has mixed data types

                if SIMPLE_EMAIL_PATTERN.match(item):
                    private_cols.append(col)
                    break  # 1 failure is enough

    return private_cols
