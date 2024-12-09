def decrypt_flag(encrypted_flag, key):
    decrypted_flag = ""
    for i in range(len(encrypted_flag)):
        # XOR it back 
        decrypted_flag += chr((ord(encrypted_flag[i]) - ord(key[i % len(key)]) + 256) % 256)
    return decrypted_flag

encrypted_flag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓÔÅÐÙí"  # Encrypted flag
key = "picoctf" 

decrypted_flag = decrypt_flag(encrypted_flag, key)
print(decrypted_flag)
