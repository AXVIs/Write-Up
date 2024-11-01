def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    decrypted = []
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - 65
            decrypted_char = chr((ord(char.upper()) - 65 - shift) % 26 + 65)
            decrypted.append(decrypted_char.lower() if char.islower() else decrypted_char)
            key_index += 1
        else:
            decrypted.append(char)

    return ''.join(decrypted)

# Ciphertext and key
ciphertext = "gwox{RgqssihYspOntqpxs}"
key = "blorpy"

# Decrypting the ciphertext
print(f"Flag: {vigenere_decrypt(ciphertext, key)}")