#!/usr/bin/env python3
"""
Module filter_datum
"""

import re
from typing import List
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    get_db - handles a connector to a mysql database
    """
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )


def get_logger() -> logging.Logger:
    """
    get_logger - creates and returns a logger named 'user_data'
    with INFO level and no propagation.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))

    logger.addHandler(stream_handler)

    return logger


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

    def __init__(self, fields: List[str]):
        """Initialize formatter with fields to redact."""
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filters values in incoming logs"""
        redacted_message = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        record.msg = redacted_message

        return super().format(record)


def main():
    """
    main - entry point, obtains a database connection through get_db(),
            retrieves all rows in the 'users' table,
            display each row, filtered
    """
    database = get_db()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = [i[0] for i in cursor.description]

    log = get_logger()

    for row in cursor:
        str_row = ''.join(f'{f}={str(r)}; ' for r, f in zip(row, fields))
        log.info(str_row.strip())

    cursor.close()
    database.close()


if __name__ == "__main__":
    main()
