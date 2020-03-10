"""
Custom errors used by PrivacyPanda
"""


class PrivacyError(RuntimeError):
    def __init__(self, message):
        super().__init__(message)
