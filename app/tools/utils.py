# app/utils.py
import string
import random

def generate_password(length: int = 10) -> str:
    """Generate a random password of given length"""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))
