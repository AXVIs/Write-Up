def polybius_decode(ciphertext):
    # Membuat Polybius square sebagai satu string
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    
    # Menghapus karakter non-numerik dan mengubah menjadi lowercase
    ciphertext = ''.join(filter(str.isdigit, ciphertext.lower()))
    
    # Mendekode setiap pasangan angka
    decoded_message = ''.join(alphabet[(int(ciphertext[i]) - 1) * 5 + (int(ciphertext[i+1]) - 1)]
                              for i in range(0, len(ciphertext), 2))
    
    return decoded_message

# Contoh penggunaan
ciphertext =  "1-3,4-4,2-1,{,4-4,2-3,4-5,3-2,1-2,4-3,_,4-5,3-5,}" 
decoded_message = polybius_decode(ciphertext)
print(f"Flag: {decoded_message[:3]}{{{decoded_message[3:9]}_{decoded_message[9:]}}}")