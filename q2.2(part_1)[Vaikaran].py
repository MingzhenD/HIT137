def separate_and_convert(s):
    # Separation between numbers and letters
    string_num = ''.join([c for c in s if c.isdigit()])
    string_num = ''.join([c for c in s if c.isalpha()])

    # Transfering even numbers to ASCII values
    even_numbers = [int(digit) for num in string_num for digit in str(num) if int(digit) % 2 == 0]
    numbers_ascii_values = [ord(str(num)) for num in even_numbers]

    # Transfering upper-case letters to ASCII values
    upper_case_letters = [char for char in string_num if char.isupper()]
    letters_ascii_values = [ord(char) for char in upper_case_letters]

    # Output visualise string separation
    print(f"Separate them - {string_num} (number string) and {string_num} (letter string).")

    # Visualise even numbers along with concequent ASCII values
    even_numbers_str = ', '.join(map(str, even_numbers))
    ascii_numbers_str = ', '.join(map(str, numbers_ascii_values))
    print(f'{even_numbers_str} (Even Numbers)')
    print(f'{ascii_numbers_str} (ASCII CODE Decimal Values)')

    # Visualise upper-case letters along with concequent ASCII values
    upper_case_letters_str = ', '.join(upper_case_letters)
    ascii_letters_str = ', '.join(map(str, letters_ascii_values))
    print(f'{upper_case_letters_str} (Upper-case Letters)')
    print(f'{ascii_letters_str} (ASCII CODE Decimal Values)')

# User input for this string
user_input = input("Enter a string (at least length of 16) containing numbers and letters: ")

# String requirement: atleast length of 16
if len(user_input) < 16:
    print("Please enter a string with a length of at least 16 characters.")
else:
    # Display the results
    separate_and_convert(user_input)
