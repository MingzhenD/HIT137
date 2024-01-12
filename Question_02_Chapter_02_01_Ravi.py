def separate_numbers_and_letters(input_string):
    # Separate numbers and letters using isdigit() and isalpha()
    numbers = ''.join(char for char in input_string if char.isdigit())
    letters = ''.join(char for char in input_string if char.isalpha())

    return numbers, letters

def convert_even_numbers_to_ascii(input_string):
    ascii_result = ''
    even_numbers = '';
    for char in input_string:
        number = int(char)
        if number % 2 == 0:
            ascii_value = ord(char)
            ascii_result += str(ascii_value) + ', '
            even_numbers += str(char) + ', '

    # Remove the trailing comma and return
    return ascii_result.rstrip(', '), even_numbers.rstrip(', ')

def convert_uppercase_letters_to_ascii(input_string):
    ascii_result = ''
    upper_letter_result = ''
    for char in input_string:
        if char.isupper():
            ascii_value = ord(char)
            ascii_result += str(ascii_value) + ', '
            upper_letter_result += char + ', '
        
    return ascii_result.rstrip(', '), upper_letter_result.rstrip(', ')

numbersList, lettersList = separate_numbers_and_letters('56aAWw1984sktr235270aYmn145ss785fsq31D0')
print('Numbers: ' + numbersList)
print('Letters: ' + lettersList)
print()

acsciis, evens = convert_even_numbers_to_ascii(numbersList)
print('Even numbers: ' + evens)
print('ASCII values: ' + acsciis)
print()

asscii_letters, upper_letters = convert_uppercase_letters_to_ascii(lettersList)
print('Upper letters: ' + upper_letters)
print('ASCII values: ' + asscii_letters)