Flag 1 - Dig all the way to the bottom to get the flag! - **cs24{compression_aggression_is_a_real_thing}**

Flag 2 - How many layers of compression are there? - **120**

---

1) The `compress.py` script will take in `flag.enc` and compresses it using bzip2, gzip, tar, and zip in a random order. The number of times it runs through are specified in the script - for this challenge, it runs through it 30 for each type.
1) `solve.sh` will read the filetype and iterate through until it reaches an ASCII filetype, at which point it does a base64 decode to get the final flag. Challengers will likely reach this point and manually decode it rather than including in a script.