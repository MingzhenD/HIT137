def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord("z"):
                    shifted -= 26
                elif shifted < ord("a"):
                    shifted += 26
            elif char.isupper():
                if shifted > ord("Z"):
                    shifted -= 26
                elif shifted < ord("A"):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, key):
    text_decrypted = ""
    for char in text:
        if char.isalpha():
            origin = ord(char) - key
            if char.islower():
                origin = (origin - ord("a")) % 26 + ord("a")
            elif char.isupper():
                origin = (origin - ord("A")) % 26 + ord("A")
            text_decrypted += chr(origin)
        else:
            text_decrypted += char
    return text_decrypted


def getKey():
    total = 0
    for i in range(5):
        for j in range(3):
            if i + j == 5:
                total += i + j
            else:
                total -= i - j
    counter = 0
    while counter < 5:
        if total < 13:
            total += 1
        elif total > 13:
            total -= 1
        else:
            counter += 2
    return total


from os import path


def main():
    # with open(path.join(path.dirname(__file__), "q3.encrypted.py")) as file_encrypted:
    #     for key in range(26):
    #         print(f"decrypt with key:{key}")
    #         with open(
    #             path.join(path.dirname(__file__), "q3.encrypted.py")
    #         ) as file_encrypted:
    #             for line in file_encrypted:
    #                 print(decrypt(line, key), end="")

    # the key is 13

    with open(path.join(path.dirname(__file__), "q3.encrypted.py")) as file_encrypted:
        with open(
            path.join(path.dirname(__file__), "q3.decrypted.py"), mode="w"
        ) as file_decrypted:
            for line in file_encrypted:
                file_decrypted.write(decrypt(line, getKey()))


main()
