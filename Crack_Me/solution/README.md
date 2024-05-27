## CRACK 1

Flag: **cs24{darthvader_pwned_123456seven_viking_n30_meowmeow123}**

`hashcat -m 500 -o out.txt crack1 /usr/share/wordlists/rockyou.txt`

```
$1$d8qBkGme$gNZFeDbg20rDdQw/ap3Zh/:darthvader
$1$VXpHmtKC$rtvIjzeg3QtBpfgEsJo/N.:pwned
$1$66dlQFzj$dFDKADbdgd/7Hs9iLM7WG1:123456seven
$1$3EWs3fw8$lXtCH8R38PUZbtLhoCw.d/:viking
$1$DsNwIwCB$GJtdNZe.zC9/CfCLkIU5L.:n30
$1$5Kes03Vp$mPOJ11NryNHCke4QAqEwl/:meowmeow123
```

---

## CRACK 2

Flag: **cs24{Ilovecats}**

`hashcat -a0 -m900 crack2 -o crack.out /usr/share/wordlists/rockyou.txt`

```
37bdde553d9e6111b9add9989c033ebb:Ilovecats
```

---

### CRACK 3

Flag: **cs24{thanks_johnny!}**

1) `zip2john crack4.zip > crack4hash`
1) `john --wordlist=/usr/share/wordlists/rockyou.txt crack4hash` - zip password: `kittycatmeow`
1) Flag is hand written in a png file

---

### CRACK 4

Flag: **cs24{ShieldConCTF}**

`cewl https://www.shieldcon.org > crack3_wordlist`

`hashcat -a1 -m3200 crack3 -o crack.out solution/crack3_wordlist solution/crack3_wordlist`

```
$2a$10$sPvQz8BbuiNTI1n8A4xi.uDfq9jbLbq43.x4cxa2xRPQP/K9nSS3e:ShieldConCTF
```