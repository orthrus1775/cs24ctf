Flag 1 - What type of cryptography is being used? - **cs24{pigpen cipher}**

Flag 2 - What is the decoded message? - **cs24{the pig says oinkoink}**

---

1) The `barnbrowser.py` script will reach out to a bunch of random barn/animal related websites, followed by a download of the `yummy.png` file. In the script, I've just hard-coded a local box hosting the image.
1) `yummy.png` is a pigpen cipher, which should be easily identified by the unique symbols
1) You can use dcode.fr to decode the cipher, which is `thepigsaysoinkoink`. The challenge site is using regex to accept with or without spaces between the words.