"""
Code for reporting the privacy of a dataframe
"""
from collections import defaultdict
from typing import TYPE_CHECKING, List, Union

from .addresses import check_addresses

if TYPE_CHECKING:
    import pandas


__all__ = ["report_privacy"]


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


def report_privacy(df: "pandas.DataFrame") -> Report:
    report = Report()

    checks = {"address": check_addresses}

    for breach, check in checks.items():
        columns = check(df)
        report.add_breach(columns, breach)

    return report
