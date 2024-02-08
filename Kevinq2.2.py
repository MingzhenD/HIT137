def separate_and_convert(s):
    numbers = ''.join(c for c in s if c.isdigit())
    letters = ''.join(c for c in s if c.isalpha())

    even_numbers_ascii = [ord(c) for c in numbers if int(c) % 2 == 0]
    upper_case_ascii = [ord(c) for c in letters if c.isupper()]

    return even_numbers_ascii, upper_case_ascii

def decrypt_cryptogram(cryptogram, shift_key):
    decrypted_text = ''
    for char in cryptogram:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - start - shift_key) % 26 + start)
        else:
            decrypted_text += char
    return decrypted_text

def calculate_letter_frequency(text):
    letter_count = {}
    total_letters = 0

    for char in text:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
            total_letters += 1

    frequency = {char: count / total_letters for char, count in letter_count.items()}
    return frequency

# Example Usage
string = '56aAww1984sktr235270aYmn145ss785fsq3100'
even_numbers, upper_case_letters = separate_and_convert(string)
print("Even Numbers ASCII Values:", even_numbers)
print("Upper Case Letters ASCII Values:", upper_case_letters)

cryptogram = 'VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR'

# Attempt to automatically find the correct shift key
best_shift_key = None
best_similarity = float('inf')
best_decrypted_text = ''

for shift_key in range(26):
    decrypted_quote = decrypt_cryptogram(cryptogram, shift_key)
    frequency = calculate_letter_frequency(decrypted_quote.upper())
    
    # Common English letter frequencies (approximate values)
    common_frequencies = {'E': 0.127, 'T': 0.091, 'A': 0.081, 'O': 0.075, 'I': 0.070}
    
    # Calculate the similarity between observed and expected frequencies
    similarity = sum((frequency.get(char, 0) - common_frequencies.get(char, 0))**2 for char in common_frequencies)
    
    # Print the decrypted text, similarity, ASCII values, and shift key for each iteration
    print(f"Shift Key = {shift_key}: {decrypted_quote} (Similarity: {similarity:.4f})")
    print(f"ASCII Values: {[ord(char) for char in decrypted_quote]}\n")
    
    # Update best shift key if the current one has higher similarity
    if similarity < best_similarity:
        best_shift_key = shift_key
        best_similarity = similarity
        best_decrypted_text = decrypted_quote

# Automatically choose the shift key with the highest similarity
print(f"\nAutomatically Chosen Shift Key: {best_shift_key}")
print(f"Decrypted Text: {best_decrypted_text}")
