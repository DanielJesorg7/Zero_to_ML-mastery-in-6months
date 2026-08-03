import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    if not (use_upper or use_lower or use_digits or use_symbols):
        return "Error: At least one character set must be selected."

    pool = ""
    mandatory_chars = []

    if use_upper:
        pool += string.ascii_uppercase
        mandatory_chars.append(random.choice(string.ascii_uppercase))
    if use_lower:
        pool += string.ascii_lowercase
        mandatory_chars.append(random.choice(string.ascii_lowercase))
    if use_digits:
        pool += string.digits
        mandatory_chars.append(random.choice(string.digits))
    if use_symbols:
        pool += string.punctuation
        mandatory_chars.append(random.choice(string.punctuation))

    if length < len(mandatory_chars):
        return "Error: Requested length is too short for the selected criteria."

    # Fill the remaining length randomly from the pool
    remaining_length = length - len(mandatory_chars)
    password_list = mandatory_chars + [random.choice(pool) for _ in range(remaining_length)]
    
    # Shuffle to ensure mandatory characters aren't always at the start
    random.shuffle(password_list)
    
    return "".join(password_list)
