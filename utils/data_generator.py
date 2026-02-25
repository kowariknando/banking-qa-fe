import random
import string

def generate_random_string(length: int = 6) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_postcode() -> str:
    prefix = random.randint(10, 99)
    suffix = random.randint(1, 9)
    return f"E{prefix} {suffix}AB"