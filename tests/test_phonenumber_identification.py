"""
Test functions for identifying phonenumbers in dataframes
"""
import pandas as pd
import pytest

import privacypanda as pp


@pytest.mark.parametrize("number", ["+447123456789", "07123456789", "07999999999"])
def test_can_identify_column_containing_correct_phonenumbers(number):
    df = pd.DataFrame(
        {"privateColumn": ["a", number, "c"], "nonPrivateColumn": ["a", "b", "c"]}
    )

    actual_private_columns = pp.check_phonenumbers(df)
    expected_private_columns = ["privateColumn"]

    assert actual_private_columns == expected_private_columns


@pytest.mark.parametrize("number", ["+4412345678", "071234567891011", "999"])
def test_number_must_have_nine_digits(number):
    # 9 digits AFTER "07"
    df = pd.DataFrame(
        {"privateColumn": ["a", number, "c"], "nonPrivateColumn": ["a", "b", "c"]}
    )

    actual_private_columns = pp.check_phonenumbers(df)
    expected_private_columns = []

    assert actual_private_columns == expected_private_columns
