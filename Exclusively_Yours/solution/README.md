Flag: **cs24{i_am_truly_yours}**

---

1) The title and source code make it obvious that this is an XOR challenge. Challengers are provided the encrypted flag in the `code.py` script, the length of the key, and the encryption code used to convert the original flag to the enc_flag.

1) Given the properties of XOR and that we have provided the flag format (cs24{flag}), you can determine the key. Once you figure out the four values by XORing with the corresponding values in the encrypted flag, you get "cs24". With the key in hand, you just need to loop through the enc_flag to decrypt the rest of the flag

1) The key should be equal to: `key = [22, 148, 17, 199]`
