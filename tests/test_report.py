"""
Test reporting functionality
"""
import numpy as np
import pandas as pd
import privacypanda as pp
import pytest


def test_can_report_addresses():
    df = pd.DataFrame(
        {
            "col1": ["a", "b", "10 Downing Street"],
            "col2": [1, 2, 3],
            "col3": ["11 Downing Street", "b", "c"],
        }
    )

    # Check correct breaches have been logged
    report = pp.report_privacy(df)
    expected_breaches = {"col1": ["address"], "col3": ["address"]}

    assert report._breaches == expected_breaches

    # Check string report
    actual_string = str(report)
    expected_string = "col1: ['address']\ncol3: ['address']\n"

    assert actual_string == expected_string


def test_can_report_phonenumbers():
    df = pd.DataFrame(
        {
            "col1": ["a", "b", "07987654321"],
            "col2": [1, 2, 3],
            "col3": ["+447123123123", "b", "c"],
        }
    )

    # Check correct breaches have been logged
    report = pp.report_privacy(df)
    expected_breaches = {"col1": ["phone number"], "col3": ["phone number"]}

    assert report._breaches == expected_breaches

    # Check string report
    actual_string = str(report)
    expected_string = "col1: ['phone number']\ncol3: ['phone number']\n"

    assert actual_string == expected_string


def test_can_report_emails():
    df = pd.DataFrame(
        {
            "col1": ["a", "b", "joe.bloggs@something.org"],
            "col2": [1, 2, 3],
            "col3": ["t.t.t@t.com", "b", "c"],
        }
    )

    # Check correct breaches have been logged
    report = pp.report_privacy(df)
    expected_breaches = {"col1": ["email"], "col3": ["email"]}

    assert report._breaches == expected_breaches

    # Check string report
    actual_string = str(report)
    expected_string = "col1: ['email']\ncol3: ['email']\n"

    assert actual_string == expected_string


def test_report_can_accept_multiple_breaches_per_column():
    df = pd.DataFrame(
        {
            "col1": ["a", "10 Downing Street", "joe.bloggs@something.org"],
            "col2": [1, 2, "AB1 1AB"],
            "col3": ["t.t.t@t.com", "b", "c"],
        }
    )
    report = pp.report_privacy(df)

    expected_breaches = {
        "col1": ["address", "email"],
        "col2": ["address"],
        "col3": ["email"],
    }

    assert report._breaches == expected_breaches


def test_check_privacy_wrapper_returns_data_if_no_privacy_breaches():
    df = pd.DataFrame({"col1": ["a", "b", "c", "d", "e"], "col2": [1, 2, 5, 10, 20]})

    @pp.check_privacy
    def return_data():
        return df

    data = return_data()

    pd.testing.assert_frame_equal(data, df)


@pytest.mark.parametrize(
    "breach_type,breach",
    [
        ("email", "a.n.email@gmail.com"),
        ("address", "10 Downing St"),
        ("phone number", "07123456789"),
    ],
)
def test_check_privacy_wrapper_raises_if_data_contains_privacy_breaches(
    breach_type, breach
):
    df = pd.DataFrame({"col1": ["a", breach, "c", "d", "e"], "col2": [1, 2, 5, 10, 20]})

    @pp.check_privacy
    def return_data():
        return df

    with pytest.raises(pp.errors.PrivacyError):
        data = return_data()


@pytest.mark.parametrize(
    "output",
    [
        5,
        [1, 2, 3],
        ("a", "b"),
        "output",
        pd.Series([1, 2, 3, 10, 15]),
        np.random.random((10, 3)),
    ],
)
def test_check_privacy_wrapper_returns_output_if_output_not_pandas_dataframe(output):
    @pp.check_privacy
    def return_data():
        return output

    data = return_data()
    assert isinstance(data, type(output))
