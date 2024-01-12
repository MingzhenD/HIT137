#Assignment 02 - Question 01 Task 03.01

from collections import Counter
import csv
import re

READ_FILE_PATH = 'allText.txt'
WRITE_FILE_PATH = 'WordsCount_Q1_T3_01.csv'
NO_OF_WORDS = 30
TITLES = ['Word', 'Count']

def count_words(text):
    # Convert text to lowercase
    text = text.lower()

    # Use regex to extract words from the text
    words = re.findall(r'\b\w+\b', text)

    # Count the occurrences of each word
    word_counts = Counter(words)

    return word_counts

def read_large_file(file_path, batch_size=10000):
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            batch = file.read(batch_size)
            if not batch:
                break
            yield batch

def process_large_file(file_path):
    all_word_counts = Counter()

    print('Reading file...')
    for batch in read_large_file(file_path):        
        word_counts = count_words(batch)
        all_word_counts += word_counts

    return all_word_counts

#Method calling
word_counts = process_large_file(READ_FILE_PATH)

# Get the top 30 most common words
top_words = word_counts.most_common(NO_OF_WORDS)

#Write result into a CSV file
with open(WRITE_FILE_PATH, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the header row
    csv_writer.writerow(TITLES)
    
    # Write the data rows    
    for row in top_words:        
        csv_writer.writerow(list(row))
        
print("Task completed")
