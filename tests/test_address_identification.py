"""
Test functions for identifying addresses in dataframes
"""
import pandas as pd
import pytest

import privacypanda as pp


@pytest.mark.parametrize("postcode", ["AB1 1AB", "AB12 1AB", "AB1    1AB"])
def test_can_identify_column_containing_UK_postcode(postcode):
    df = pd.DataFrame(
        {"privateColumn": ["a", postcode, "c"], "nonPrivateColumn": ["a", "b", "c"]}
    )

    actual_private_columns = pp.check_addresses(df)
    expected_private_columns = ["privateColumn"]

    assert actual_private_columns == expected_private_columns


@pytest.mark.parametrize(
    "address",
    [
        "10 Downing Street",
        "10 downing street",
        "1 the Road",
        "01 The Road",
        "1234 The Road",
        "55 Maple Avenue",
        "4 Python Way",
    ],
)
def test_can_identify_column_containing_simple_street_names(address):
    df = pd.DataFrame(
        {"privateColumn": ["a", address, "c"], "nonPrivateColumn": ["a", "b", "c"]}
    )

    actual_private_columns = pp.check_addresses(df)
    expected_private_columns = ["privateColumn"]

    assert actual_private_columns == expected_private_columns


def test_address_check_returns_empty_list_if_no_addresses_found():
    df = pd.DataFrame(
        {"nonPrivateColumn1": ["a", "b", "c"], "nonPrivateColumn2": ["a", "b", "c"]}
    )

    actual_private_columns = pp.check_addresses(df)
    expected_private_columns = []

    assert actual_private_columns == expected_private_columns


def test_check_addresses_can_handle_mixed_dtype_columns():
    df = pd.DataFrame(
        {
            "privateColumn": [True, "AB1 1AB", "c"],
            "privateColumn2": [1, "b", "10 Downing Street"],
            "nonPrivateColumn": [0, True, "test"],
        }
    )

    actual_private_columns = pp.check_addresses(df)
    expected_private_columns = ["privateColumn", "privateColumn2"]

    assert actual_private_columns == expected_private_columns
