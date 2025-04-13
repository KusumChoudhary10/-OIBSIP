import random
import string

def generate_password(length=12):
    if length < 4:
        return "Password too short. Minimum length is 4."
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

print(generate_password(12))
