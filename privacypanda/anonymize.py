"""
Code for cleaning a dataframe of private data
"""
import pandas as pd
from numpy import unique as np_unique

from .addresses import check_addresses


def anonymize(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove private data from a dataframe

    Any column containing at least one piece of private data is removed from
    the dataframe. This is a naive solution but limits the possibility of
    false negatives.

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe to anonymize

    Returns
    -------
    pd.DataFrame
        The dataframe with columns containing private data removed
    """
    private_cols = []

    checks = [check_addresses]
    for check in checks:
        new_private_cols = check(df)
        private_cols += new_private_cols

    # Get unique columns
    private_cols = np_unique(private_cols).tolist()

    # Drop columns
    return df.drop(private_cols, axis=1)
