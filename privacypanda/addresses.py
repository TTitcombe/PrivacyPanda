"""
Code for identifying addresses
"""
import re
from typing import List

import numpy as np
import pandas as pd

OBJECT_DTYPE = np.dtype("O")

# ----- Regex constants ----- #
LETTER = "[a-zA-Z]"

# UK Postcode
UK_POSTCODE_PATTERN = re.compile(
    LETTER + LETTER + "\\d{1,2}" + "\\s+" + "\\d" + LETTER + LETTER
)

# Street names
STREET_ENDINGS = "[street|road|way|avenue]"

# Simple address is up to a four digit number + street name with 1-10 characters
# + one of "road", "street", "way", "avenue"
SIMPLE_ADDRESS_PATTERN = re.compile(
    "[0-9]{1,4}\\s[a-z]{1,10}\\s" + STREET_ENDINGS, re.I
)


def check_addresses(df: pd.DataFrame) -> List:
    """
    Check a dataframe for columns containing addresses. Returns a list of column
    names which contain at least one address

    "Addresses" currently only concerns UK postcodes and simple street names.
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

                if UK_POSTCODE_PATTERN.match(item) or SIMPLE_ADDRESS_PATTERN.match(
                    item
                ):
                    private_cols.append(col)
                    break  # 1 failure is enough

    return private_cols
