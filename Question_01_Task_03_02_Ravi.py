from collections import Counter
from transformers import AutoTokenizer

READ_FILE_PATH = 'allText.txt'
WRITE_FILE_PATH = 'top30Tokens_Q1_T3_02.txt'
MODEL_NAME = 'alvaroalon2/biobert_diseases_ner' 

def count_and_get_top_tokens(model_name, file_path, batch_size=10000, top_n=30):
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Initialize counters
    total_unique_tokens = set()

    # Process the file in batches
    print('Reading file...')
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            batch = file.read(batch_size)
            if not batch:
                break  # End of file

            # Tokenize the batch            
            tokens = tokenizer.tokenize(batch)

            # Update total unique tokens
            total_unique_tokens.update(set(tokens))

    # Get the top N unique tokens
    top_unique_tokens = Counter(total_unique_tokens).most_common(top_n)
    return top_unique_tokens

#Method calling
top_unique_tokens = count_and_get_top_tokens(MODEL_NAME, READ_FILE_PATH)

#write to a .txt file
open(WRITE_FILE_PATH, "w").close()
print("Writing to file...")
for index, (token, count) in enumerate(top_unique_tokens):
    token_str = f"Token {(index + 1)}: {token}"    
    with open(WRITE_FILE_PATH, 'a') as the_file:
            the_file.writelines(token_str + '\n')

print('Task completed')
