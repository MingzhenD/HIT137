# github link
# https://github.com/MingzhenD/HIT137.git
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


# encrypted text:
encrypted_code='''
tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inevnoyr)
        ybpny_inevnoyr -= 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xrl4'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
'''

# from os import path
def main():
    # the key is 13
    print(decrypt(encrypted_code, getKey()))
main()

#################################### recorrected and comments ##################################
global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Add default parameter: numbers with value [1, 2, 3, 4, 5]
def process_numbers(numbers = list(range(1,6))):
    global global_variable
    # change to length of given list/set
    local_variable = len(numbers)

    while local_variable > 0:
        # check if the collection contains the value before remove it
        if local_variable % 2 == 0 and local_variable in numbers:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

# Set items are unordered, unchangeable, and do not allow duplicate values.
my_set = {1, 2, 3, 4, 5}
result = process_numbers(numbers=my_set)

# add parameter of this function to modify the dictionary key with default value None
def modify_dict(key, value=None):
    my_dict[key] = value

# modify key4, 10 in my_dict
modify_dict('key4', 10)
# add '5: None' in my_dict
modify_dict(5)

def update_global():
    global global_variable
    global_variable += 10

# call the function by name and parentheses to modify global variable
update_global()

for i in range(5):
    print(i)
    i += 1

if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")

# check if key set contains 5
if 5 not in my_dict:
    print("5 not found in the dictionary!")

# check if value list contains 10
if 10 not in my_dict.values():
    print("10 not found in the dictionary values!")

print(global_variable)
print(my_dict)
print(my_set)
