def decrypt_interval(encrypted_message, interval):
    decrypted = ""
    for i in range(0, len(encrypted_message), interval):
        decrypted += encrypted_message[i]
    return decrypted

# Test
msg = "sxeyxnxycdyxhxeyxyesxyxe"
interval = 2
print(decrypt_interval(msg, interval))  # sendcheese