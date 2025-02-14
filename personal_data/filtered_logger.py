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
    """
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}',
                         message)
    return message
