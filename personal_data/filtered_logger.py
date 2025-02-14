#!/usr/bin/env python3
"""
Module filter_datum
"""

import re

def filter_datum(fields, redaction, message, separator):
    """
    filter_datum - module that returns a log message offuscated
    :param fields: list[str] - representes all fields to obfuscate
    :param redaction: str - represents by what the field will be obfuscated
    :param message: str - the log line
    :param separator: str - elements that separates each fields
    """
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                        f'{field}={redaction}{separator}',
                        message)
    return message


