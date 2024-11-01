def shift_right_qwerty(char):
    qwerty = "qwertyuiopasdfghjkl;zxcvbnm,./QWERTYUIOPASDFGHJKL:ZXCVBNM<>?1234567890!@#$%^&*()-_=+"
    shifted = "wertyuiopasdfghjkl;zxcvbnm,./qwertyuiopasdfghjkl;ZXCVBNM<>?1234567890!@#$%^&*()-_=+q"
    
    if char in qwerty:
        return shifted[qwerty.index(char)]
    return char

def decrypt_keyboard_shift(ciphertext, shift=2):
    decrypted_text = ''.join(shift_right_qwerty(char) for char in ciphertext)
    return decrypted_text

# Ciphertext yang ingin di-decrypt
ciphertext = "BUH'tdy,|Bim5y~Bdt76yQ"
decrypted_text = decrypt_keyboard_shift(ciphertext)

print(decrypted_text)