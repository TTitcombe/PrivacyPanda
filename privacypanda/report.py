"""
Code for reporting the privacy of a dataframe
"""
from collections import defaultdict
from typing import TYPE_CHECKING, Callable, List, Union

import pandas as pd

from .addresses import check_addresses
from .email import check_emails
from .errors import PrivacyError
from .phonenumbers import check_phonenumbers

__all__ = ["report_privacy", "check_privacy"]


class Report:
    def __init__(self):
        self._breaches = defaultdict(list)

    def add_breach(self, columns: Union[List[str], str], breach: str):
        """
        Add columns which breach privacy to the dictionary of breaches

        Parameters
        ----------
        columns : list of strings or a string
            A single column or a list of columns which have breached privacy
        breach : str
            A type of breach

        Returns
        -------
        None

        Raises
        ------
        AssertionError
            If breach not "address", "name", "email", "phone number"
        """
        breach = breach.lower()
        valid_breaches = ("address", "name", "email", "phone number")
        assert breach in valid_breaches, f"{breach} not in {valid_breaches}"

        if isinstance(columns, str):
            columns = [columns]

        for column in columns:
            self._breaches[column].append(breach)

    def __str__(self):
        report = ""
        for column, breaches in self._breaches.items():
            report += f"{column}: {breaches}\n"
        return report


def report_privacy(df: pd.DataFrame) -> Report:
    """
    Create a Report on the privacy of a dataframe

    Parameters
    ----------
    df : pandas.DataFrame
        The data on which to create a report

    Returns
    -------
    privacypanda.report.Report
        The report object on the provided dataframe
    """
    report = Report()

    checks = {
        "address": check_addresses,
        "email": check_emails,
        "phone number": check_phonenumbers,
    }

    for breach, check in checks.items():
        columns = check(df)
        report.add_breach(columns, breach)

    return report


# Privacy decorator
def check_privacy(func: Callable) -> Callable:
    """
    A decorator which checks if the output of a function
    breaches privacy

    Parameters
    ----------
    func : function
        The function to wrap

    Returns
    -------
    The function, wrapped so function output
    is checked for privacy breaches

    Raises
    ------
    PrivacyError
        If the output of the wrapped function breaches privacy
    """

    def inner_func(*args, **kwargs):
        data = func(*args, **kwargs)

        if isinstance(data, pd.DataFrame):
            privacy_report = report_privacy(data)

            if privacy_report._breaches.keys():
                # Output list of breaches
                breaches = f""
                for breach_col, breach_type in privacy_report._breaches.items():
                    breaches += f"\t{breach_col}: {breach_type}\n"

                raise PrivacyError("Privacy breach in data:\n" + breaches)

        return data

    return inner_func
