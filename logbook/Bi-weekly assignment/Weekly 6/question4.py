def encrypt_simple(message):
    no_spaces = message.replace(" ", "")
    return no_spaces[::-1]

# Test
print(encrypt_simple("hello world"))  # dlrowolleh