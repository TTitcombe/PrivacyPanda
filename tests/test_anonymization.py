"""
Test functions for anonymizing dataframes
"""
import pandas as pd
import pytest

import privacypanda as pp


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
        "AB1 1AB",
        "AB12 1AB",
    ],
)
def test_removes_columns_containing_addresses(address):
    df = pd.DataFrame(
        {
            "privateData": ["a", "b", "c", address],
            "nonPrivateData": ["a", "b", "c", "d"],
            "nonPrivataData2": [1, 2, 3, 4],
        }
    )

    expected_df = pd.DataFrame(
        {"nonPrivateData": ["a", "b", "c", "d"], "nonPrivataData2": [1, 2, 3, 4]}
    )

    actual_df = pp.anonymize(df)

    pd.testing.assert_frame_equal(actual_df, expected_df)


@pytest.mark.parametrize(
    "email",
    [
        "a.test.email@email.com",
        "a.n.other@testing.co.uk",
        "a.person@blah.org",
        "foo@bar.edu",
    ],
)
def test_removes_columns_containing_emails(email):
    df = pd.DataFrame(
        {
            "privateData": ["a", "b", "c", email],
            "nonPrivateData": ["a", "b", "c", "d"],
            "nonPrivataData2": [1, 2, 3, 4],
        }
    )

    expected_df = pd.DataFrame(
        {"nonPrivateData": ["a", "b", "c", "d"], "nonPrivataData2": [1, 2, 3, 4]}
    )

    actual_df = pp.anonymize(df)

    pd.testing.assert_frame_equal(actual_df, expected_df)


def test_returns_empty_dataframe_if_all_columns_contain_private_information():
    df = pd.DataFrame(
        {
            "nonPrivateData": ["a", "AB1 1AB", "c", "d"],
            "PrivataData2": [1, 2, 3, "AB1 1AB"],
        }
    )

    expected_df = pd.DataFrame(index=[0, 1, 2, 3])
    actual_df = pp.anonymize(df)

    pd.testing.assert_frame_equal(actual_df, expected_df)
