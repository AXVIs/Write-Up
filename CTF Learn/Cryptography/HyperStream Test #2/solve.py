def bacon_decrypt(ciphertext):
    # I=J & U-V
    bacon_24letters = {
        'aaaaa': 'A', 'aaaab': 'B', 'aaaba': 'C', 'aaabb': 'D',
        'aabaa': 'E', 'aabab': 'F', 'aabba': 'G', 'aabbb': 'H',
        'abaaa': 'I', 'abaab': 'K', 'ababa': 'L', 'ababb': 'M', 
        'abbaa': 'N', 'abbab': 'O', 'abbba': 'P', 'abbbb': 'Q', 
        'baaaa': 'R', 'baaab': 'S', 'baaba': 'T', 'baabb': 'U', 
        'babaa': 'W', 'babab': 'X', 'babba': 'Y', 'babbb': 'Z', 
        ' ': ' '
    }

    ciphertext = ciphertext.lower()
    
    # Split the ciphertext into groups of 5 and decrypt
    return ''.join(bacon_24letters[ciphertext[i:i+5]] for i in range(0, len(ciphertext), 5))

# Example ciphertext
ciphertext = "ABAAAABABAABBABBAABBAABAAAAAABAAAAAAAABAABBABABBAAAAABBABBABABBAABAABABABBAABBABBAABB"
# Decrypting the ciphertext
print(f"Flag: CTFlearn{{{bacon_decrypt(ciphertext)}}}")