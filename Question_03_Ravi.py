total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i + j # i - j will not do the expected calculation

counter = 0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2

#encrypted code
encrypted_text = ""
encrypted_text += "tybony_inevnoyr = 100 "
encrypted_text += "zl_qvpg = {'xr11': 'inyhr1', 'xr12': 'inyhr2', 'xr13': 'inyhr3'} "
encrypted_text += " "
encrypted_text += "qrs cebprff_ahzoref(): "
encrypted_text += "  tybony tybony_inevnoyr "
encrypted_text += "  ybpny_inevnoyr = 5 "
encrypted_text += "  ahzoref= [1, 2, 3, 4, 5] "
encrypted_text += " "
encrypted_text += "  juvyr ybpny_inevnoyr > 0: "
encrypted_text += "      vs ybpny_inevnoyr % 2 == 0: "
encrypted_text += "          ahzoref.erzbir(ybpny_inevnoyr) "
encrypted_text += "      ybpny_inevnoyr -= 1 "
encrypted_text += " "
encrypted_text += "  erghea ahzoref "
encrypted_text += " "
encrypted_text += "zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} "
encrypted_text += "erfhyg = cebprff_ahzoref (ahzoref=zl_frg) "
encrypted_text += " "
encrypted_text += "qrs zbqvsl_qvpg(): "
encrypted_text += "  ybpny_inevnoyr = 10 "
encrypted_text += "  zl_qvpg['xr14'] = ybpny_inevnoyr "
encrypted_text += " "
encrypted_text += "zbqvsl_qvpg(5) "
encrypted_text += " "
encrypted_text += "qrs hcqngr_tybony(): "
encrypted_text += "  tybony tybony_inevnoyr "
encrypted_text += "  tybony_inevnoyr += 10 "
encrypted_text += " "
encrypted_text += "sbe v va enatr(5): "
encrypted_text += "  cevag(v) "
encrypted_text += "  V += 1 "
encrypted_text += " "
encrypted_text += "vs z1_frg vf abg Abar naq z1_qvpg['xr14'] == 10: "
encrypted_text += "  cevag('Pbaqvgvba zrg!') "
encrypted_text += " "
encrypted_text += "vs 5 abg va z1_qvpg: "
encrypted_text += "  cevag('5 abg sbhaq va gur qvpgvbanel!') "
encrypted_text += " "
encrypted_text += "cevag(tybony_inevnoyr) "
encrypted_text += "cevag(z1_qvpg) "
encrypted_text += "cevag(zl_frg) "

#encrypt method
def encrypt(text, key): 
    encrypted_text = ""
    for char in text: 
        if char.isalpha():
            shifted = ord(char) + key 
            if char.islower():
                if shifted > ord('z'): 
                    shifted -= 26
                elif shifted < ord('a'): 
                    shifted + 26
            elif char.isupper():
                if shifted > ord('Z'): 
                    shifted -= 26
            elif shifted < ord('A'):
                shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

#decrypt method
def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

key = total
decrypted_code = decrypt(encrypted_text, key)
print(f'Key: {key}')
print('Decrypted code: ')
print(decrypted_code)



#decrypted code
global_variable = 100 
my_dict = {'ke11': 'value1', 'ke12': 'value2', 'ke13': 'value3'}  

def process_numbers(numbers): #missing parameter added
    global global_variable   
    local_variable = 5   
    numbers = numbers #[1, 2, 3, 4, 5] existing array replaced with parameter value
    
    while local_variable > 0:       
        if local_variable % 2 == 0:           
            numbers.remove(local_variable)       
        local_variable -= 1    
            
    return numbers  

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} 
result = process_numbers (numbers=my_set)  

def modify_dict():   
    local_variable = 10  
    my_dict['ke14'] = local_variable  
    
modify_dict()  #passed parameter removed, the method does not expect any parameter

def update_global():   
    global global_variable   
    global_variable += 10  
    
for i in range(5):   
    print(i)   
    i += 1  # capital (I) is not defined, it should be simple (i)
    
if my_set is not None and my_dict['ke14'] == 10:  #m1_set should be my_set, and m1_dict should be my_dict
    print('Condition met!')  
    
if 5 not in my_dict:    #m1_dict should be my_dict
    print('5 not found in the dictionary!')  
    
print(global_variable) 
print(my_dict) #m1_dict should be my_dict
print(my_set)
