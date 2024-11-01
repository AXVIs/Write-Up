def atbash_cipher(text):
    # Define the alphabet
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Create the Atbash translation table
    reversed_alphabet = alphabet[::-1]
    atbash_table = str.maketrans(alphabet + alphabet.lower(), reversed_alphabet + reversed_alphabet.lower())
    
    # Apply the cipher using the translation table
    return text.translate(atbash_table)

# Example usage
ciphertext = atbash_cipher("XGUIHG{4gy4hs_x0w3}")
print(f"Flag: {ciphertext}")