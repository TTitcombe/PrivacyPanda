"""
Code for cleaning a dataframe of private data
"""
from typing import TYPE_CHECKING, Dict, Tuple

from numpy import unique as np_unique

from .addresses import check_addresses
from .email import check_emails
from .phonenumbers import check_phonenumbers

if TYPE_CHECKING:
    import pandas


def anonymize(df: "pandas.DataFrame") -> "pandas.DataFrame":
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

    checks = [check_addresses, check_emails, check_phonenumbers]
    for check in checks:
        new_private_cols = check(df)
        private_cols += new_private_cols

    # Get unique columns
    private_cols = np_unique(private_cols).tolist()

    # Drop columns
    return df.drop(private_cols, axis=1)


def unique_id(
    data: "pandas.DataFrame", column: str, id_mapping=None
) -> Tuple["pandas.DataFrame", Dict[str, int]]:
    """
    Replace data in a given column of a dataframe with a unique id.

    Parameters
    ----------
    data : pandas.DataFrame
        The data to anonymise
    column : str
        The name of the column in data to be anonymised
    id_mapping : dict, optional
        Existing unique ID mappings to use. If not provided, start mapping from scratch

    Returns
    -------
    pandas.DataFrame
        The given data, but with the data in the given column mapped to a unique id
    dict
        The mapping of non-private data to unique IDs
    """
    if id_mapping is None:
        id_mapping = {}

    current_max_id = max(id_mapping.values())

    for idx in data.shape[0]:
        datum = data[idx, column]

        if isinstance(datum, str):
            # Assume it's an ID already
            continue

        try:
            id = id_mapping[datum]
        except KeyError:
            current_max_id += 1
            id_mapping[datum] = current_max_id
            data[idx, column] = current_max_id
        else:
            data[idx, column] = id

    return data, id_mapping
