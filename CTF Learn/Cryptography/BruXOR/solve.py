from pwn import *
ciphertext = "q{vpln'bH_varHuebcrqxetrHOXEj"

for key in range(256):
    decrypted = xor(ciphertext, key)
    try:
        decrypted_text = decrypted.decode()

        if 'flag' in decrypted_text:
            print(f"Key: {key} -> Flag: {decrypted_text}")
                        
    except UnicodeDecodeError:
        continue