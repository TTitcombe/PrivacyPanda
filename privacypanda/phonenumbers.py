"""
Code for identifying phonenumbers
"""
import re
from typing import List

import pandas as pd
from numpy import dtype as np_dtype

__all__ = ["check_phonenumbers"]

OBJECT_DTYPE = np_dtype("O")

# REGEX
NUMBER_PREFIX = r"(\+44|0)7"

# A simple UK phone number is +447 or 07, followed by 9 digits
SIMPLE_UK_MOBILE = re.compile(NUMBER_PREFIX + "[0-9]{9}")


def check_phonenumbers(df: pd.DataFrame) -> List:
    """
    Check a dataframe for columns containing phonenumbers. Returns a list of column
    names which contain at least one address

    "Addresses" currently only concerns UK mobile numbers. These begin with
    +44/0 7, then 9 digits.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to check

    Returns
    -------
    List
        The names of columns which contain at least one phonenumber
    """
    private_cols = []

    for col in df:
        row = df[col]

        # Only check column if it may contain strings
        if row.dtype == OBJECT_DTYPE:
            for item in row:
                item = str(item)  # convert incase column has mixed data types

                if SIMPLE_UK_MOBILE.fullmatch(item):
                    private_cols.append(col)
                    break  # 1 failure is enough

    return private_cols
