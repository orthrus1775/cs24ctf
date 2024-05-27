flag = "cs24{xxxxxxxxxxxxxxxx}"
enc_flag = [117, 231, 35, 243, 109, 253, 78, 166, 123, 203, 101, 181, 99, 248, 104, 152, 111, 251, 100, 181, 101, 233]
key = [0, 0, 0, 0]

def encrypt_flag(flag, key):
    encrypted_flag = []
    for idx, char in enumerate(flag):
        encrypted_char = ord(char) ^ key[idx % len(key)]
        encrypted_flag.append(encrypted_char)
    return encrypted_flag

# Encrypt the flag
enc_flag = encrypt_flag(flag, key)
print("Encrypted flag:", enc_flag)