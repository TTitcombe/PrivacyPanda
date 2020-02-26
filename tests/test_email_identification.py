"""
Test functions for identifying emails in dataframes
"""
import pandas as pd
import pytest

import privacypanda as pp


@pytest.mark.parametrize(
    "email",
    ["test@testing.com", "test@testing.co.uk", "test@testing.org", "test@testing.edu"],
)
def test_can_identify_column_whitelisted_suffixes(email):
    df = pd.DataFrame(
        {"privateColumn": ["a", email, "c"], "nonPrivateColumn": ["a", "b", "c"]}
    )

    actual_private_columns = pp.check_emails(df)
    expected_private_columns = ["privateColumn"]

    assert actual_private_columns == expected_private_columns


def test_address_check_returns_empty_list_if_no_emails_found():
    df = pd.DataFrame(
        {"nonPrivateColumn1": ["a", "b", "c"], "nonPrivateColumn2": ["a", "b", "c"]}
    )

    actual_private_columns = pp.check_emails(df)
    expected_private_columns = []

    assert actual_private_columns == expected_private_columns


def test_check_emails_can_handle_mixed_dtype_columns():
    df = pd.DataFrame(
        {
            "privateColumn": [True, "a.name@gmail.com", "c"],
            "privateColumn2": [1, "b", "j.o.blogg@harvard.edu"],
            "nonPrivateColumn": [0, True, "test"],
        }
    )

    actual_private_columns = pp.check_emails(df)
    expected_private_columns = ["privateColumn", "privateColumn2"]

    assert actual_private_columns == expected_private_columns
