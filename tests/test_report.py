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


def test_report_can_accept_multiple_breaches_per_column():
    report = pp.report.Report()

    report.add_breach("col1", "address")
    report.add_breach("col1", "phone number")

    expected_breaches = {"col1": ["address", "phone number"]}

    assert report._breaches == expected_breaches
