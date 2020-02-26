"""
Test reporting functionality
"""
import pandas as pd
import pytest

import privacypanda as pp


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
