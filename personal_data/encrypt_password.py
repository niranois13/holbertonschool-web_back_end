#!/usr/bin/env python3
'''
modules hash_password and is_valid
'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''
    hash_password - function that hashes a password for security with bcrypt

    :param password: str - a string containing the password to hash

    Returns: the hashed password as a byte string
    '''
    pass_encoded = password.encode()
    pass_hashed = bcrypt.hashpw(pass_encoded, bcrypt.gensalt())

    return pass_hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    is_valid - compares a password to its hash to compare its validity

    :param hashed_password: bytes - the hashed password to check against
    :param password: str - plain text password to be checked for validity

    Returns: boolean - True if password valid otherwise False
    '''
    valid = False
    pass_encoded = password.encode()
    if bcrypt.checkpw(pass_encoded, hashed_password):
        valid = True
    return valid
