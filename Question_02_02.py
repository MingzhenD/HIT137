# github link
# https://github.com/MingzhenD/HIT137.git
raw_str = input("input string:")
# raw_str = "56aAww1984sktr235270aYmn145ss785fsq31D0"

print(raw_str)
num_str = ""
letter_str = ""
for char in raw_str:
    char_ord = ord(char)
    if char_ord >= 48 and char_ord <= 57:
        num_str += char
    else:
        letter_str += char

print("number string:", format(num_str))
print("letter string:", format(letter_str))
num_even = []
num_ascii = []
for num in num_str:
    numInt = int(num)
    if numInt % 2 == 0:
        num_even.append(numInt)
        num_ascii.append(ord(num))
print("even number:", num_even)
print("ASCII codes:", num_ascii)

letter_upper = []
letter_ascii = []

for char in letter_str:
    char_ord = ord(char)
    if char_ord >= ord("A") and char_ord <= ord("Z"):
        letter_upper.append(char)
        letter_ascii.append(char_ord)

print("Upper-case letter:", letter_upper)
print("ASCII codes:", letter_ascii)
