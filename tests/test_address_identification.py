"""
Test functions for identifying addresses in dataframes
"""
import pandas as pd
import pytest

import privacypanda as pp


def test_can_identify_column_containing_simple_UK_postcode():
    df = pd.DataFrame(
        {"privateColumn": ["a", "AB1 1AB", "c"], "nonPrivateColumn": ["a", "b", "c"]}
    )

    actual_private_columns = pp.check_addresses(df)
    expected_private_columns = ["privateColumn"]

    assert actual_private_columns == expected_private_columns


def test_can_identify_column_containing_simple_UK_postcode_with_extra_digit():
    df = pd.DataFrame(
        {"privateColumn": ["a", "AB12 1AB", "c"], "nonPrivateColumn": ["a", "b", "c"]}
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


def test_identifies_UK_postcode_with_tab_separated_sections():
    df = pd.DataFrame(
        {"privateColumn": ["a", "AB12   1AB", "c"], "nonPrivateColumn": ["a", "b", "c"]}
    )

    actual_private_columns = pp.check_addresses(df)
    expected_private_columns = ["privateColumn"]

    assert actual_private_columns == expected_private_columns
