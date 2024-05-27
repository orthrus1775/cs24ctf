# Known part of the plaintext flag
known_plaintext = "cs24"

# Encrypted flag
enc_flag = [117, 231, 35, 243, 109, 253, 78, 166, 123, 203, 101, 181, 99, 248, 104, 152, 111, 251, 100, 181, 101, 233]

# Function to find the key
def find_key(known_plaintext, enc_flag):
    key = []
    for idx, char in enumerate(known_plaintext):
        enc_char = enc_flag[idx]
        key_char = ord(char) ^ enc_char # determine what value, when XOR'd with the encrypted value, results in "cs24"
        key.append(key_char)
    return key

# Find the key using the known part of the plaintext flag
key = find_key(known_plaintext, enc_flag)
print("Found key:", key)

# Extend the key to match the length of the encrypted flag
key_length = len(key)
extended_key = key * (len(enc_flag) // key_length) + key[:len(enc_flag) % key_length]

# Function to decrypt the flag
def decrypt_flag(enc_flag, key):
    decrypted_flag = ""
    for idx, enc_char in enumerate(enc_flag):
        decrypted_char = chr(enc_char ^ key[idx])
        decrypted_flag += decrypted_char
    return decrypted_flag

# Decrypt the entire flag using the found key
decrypted_flag = decrypt_flag(enc_flag, extended_key)
print("Decrypted flag:", decrypted_flag)
