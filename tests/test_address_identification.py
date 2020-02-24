"""
Test functions for identifying addresses in dataframes
"""
import pandas as pd
import pytest

import privacypanda as pp


def test_can_identify_column_containing_simple_postcode():
    df = pd.DataFrame(
        {"privateColumn": ["a", "AB1 1AB", "c"], "nonPrivateColumn": ["a", "b", "c"]}
    )

    actual_private_columns = pp.check_addresses(df)
    expected_private_columns = ["privateColumn"]

    assert actual_private_columns == expected_private_columns
