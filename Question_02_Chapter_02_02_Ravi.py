import nltk
from nltk.corpus import words

CIPHER_TEXT = 'VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFGZNEVYLA ZBAEBR'

# Download the 'words' resource if not already downloaded
nltk.download('words')
nltk.download('punkt')

def find_shift_key(cyphered_text):
    cyphered_text = cyphered_text.upper()
    is_key_found = 0
    print('Processeing...')
    for shift in range(100):
        decrypted_text = decrypt_cipher(cyphered_text, -shift)
        if(is_meaningful(decrypted_text)):
            is_key_found = 1
            print(f'Shift Key: {shift:2}')
            print(f'Decrypted Text: {decrypted_text}')
            break
    if is_key_found == 0:
        print('Could not find the shift key')

def decrypt_cipher(input_string, shift_key):
    result = ''

    for char in input_string:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift_key) % 26 + ord('A' if is_upper else 'a'))
            result += shifted_char
        else:
            result += char

    return result

def is_meaningful(text):
    # Get the set of English words
    english_word_set = set(words.words())

    # Tokenize the input text into words
    word_tokens = nltk.word_tokenize(text.lower())  # Convert to lowercase for case-insensitive comparison

    # Check the percentage of words in the English words set
    meaningful_word_count = sum(1 for word in word_tokens if word in english_word_set)
    percentage_meaningful = (meaningful_word_count / len(word_tokens)) * 100

    # Adjust the threshold based on requirements
    threshold = 70  

    return percentage_meaningful >= threshold

#Method calling
find_shift_key(CIPHER_TEXT)




