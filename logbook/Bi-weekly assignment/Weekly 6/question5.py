import random
import string

def encrypt_interval(message):
    interval = random.randint(2, 20)
    encrypted = ""

    for char in message:
        encrypted += char
        for _ in range(interval - 1):
            encrypted += random.choice(string.ascii_lowercase)

    return encrypted, interval

# Test
encrypted_message, used_interval = encrypt_interval("send cheese")
print("Encrypted:", encrypted_message)
print("Interval:", used_interval)