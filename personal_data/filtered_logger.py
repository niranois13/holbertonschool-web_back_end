#!/usr/bin/env python3
"""
Module filter_datum
"""

import re
from typing import List
import logging



def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ Filters values in incoming logs"""
        redacted_message = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        record.msg = redacted_message
        
        return super().format(record)
