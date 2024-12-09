def caeser_decrypt(ciphertext, shift): 
    """Decrypt from base64."""
    decrypted = [] 
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            decrypted.append(char)

    return ''.join(decrypted)
    
ciphertext = "wpjvJAM{jhlzhy_k3jy9wa3k_m0212758}"
print(caeser_decrypt(ciphertext, 7))