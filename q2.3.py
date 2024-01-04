encrypted = """VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR V NZ BHG BS PBAGEBY
NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"""

print(encrypted)


def decrypt(str, offset=0):
    decrypted = ""
    for char in str:
        if ord(char) >= ord("A") and ord(char) <= ord("Z"):
            origin_ord = (ord(char) + offset - ord("A")) % 26 + ord("A")
            decrypted += chr(origin_ord)
        elif ord(char) >= ord("a") and ord(char) <= ord("z"):
            origin_ord = (ord(char) + offset - ord("a")) % 26 + ord("a")
            decrypted += chr(origin_ord)
        else:
            decrypted += char
    return decrypted


# for i in range(26):
#     print(f"decrypted with shift {i}:")
#     decrypted = decrypt(encrypted, i)
#     print(decrypted)

# the shift is 13
print("shift 13:", decrypt(encrypted, 13))
