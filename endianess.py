def find_little_endian(word): 
    little_endian = ""

    for char in reversed(word):
        little_endian += f"{ord(char):02X}"

    return little_endian

def find_big_endian(word): 
    big_endian = ""

    for char in word:
        big_endian += f"{ord(char):02X}"

    return big_endian

print(find_little_endian("drjld"))
print(find_big_endian("drjld"))