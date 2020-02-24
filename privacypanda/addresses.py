"""
Code for identifying addresses
"""
import re
from typing import List

import numpy as np
import pandas as pd

OBJECT_DTYPE = np.dtype("O")

# Regex constants
LETTER = "[a-zA-Z]"
UK_POSTCODE_PATTERN = re.compile(
    LETTER + LETTER + "\\d{1,2}" + "\\s+" + "\\d" + LETTER + LETTER
)


def check_addresses(df: pd.DataFrame) -> List:
    """
    Check a dataframe for columns containing addresses. Returns a list of column
    names which contain at least one address

    "Addresses" currently only concerns UK postcodes, which are of the form:
    * Two letters
    * One or two digits
    * Whitespace
    * One digit
    * Two letters
    E.g.:
    * AB1 1AB
    * AB12 1AB
    This implementation does not consider whether the addresses are real.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to check

    Returns
    -------
    List
        The names of columns which contain at least one address

    """
    private_cols = []

    for col in df:
        row = df[col]

        # Only check column if it may contain strings
        if row.dtype == OBJECT_DTYPE:
            for item in row:

                if UK_POSTCODE_PATTERN.match(item):
                    private_cols.append(col)
                    break  # 1 failure is enough

    return private_cols
