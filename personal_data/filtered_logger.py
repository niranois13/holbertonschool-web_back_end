#!/usr/bin/env python3
"""
Module filter_datum
"""

import re


def filter_datum(
        fields: list[str], redaction: str, message: str, separator: str
        ) -> str:
    """
    filter_datum - module that returns a log message offuscated
    :param fields: list[str] - representes all fields to obfuscate
    :param redaction: str - represents by what the field will be obfuscated
    :param message: str - the log line
    :param separator: str - elements that separates each fields
    """
    for field in fields:
        pattern = rf'{re.escape(field)}=[^ {re.escape(separator)}]*'
        message = re.sub(pattern, f'{field}={redaction}', message)
    return message
