import csv
import spacy
from transformers import pipeline

READ_FILE_PATH = 'ALLTEXT.txt'
WRITE_FILE_PATH = 'Entities_Q1_T4_Out.csv'

BIOBERT_DISEASE_MODEL_NAME = 'alvaroalon2/biobert_diseases_ner' 
BIOBERT_CHEMICAL_MODEL_NAME = 'alvaroalon2/biobert_chemical_ner'

TITLES = ['Biobert Diseases', 'Biobert Chemicals', 'Scispacy Diseases', 'Scispacy Chemicals']

# Load the biomedical model
nlp_bc5cdr = spacy.load('en_ner_bc5cdr_md')

#Method
def get_diseases_and_chemicals(file_path, batch_size=10000):
    # Load the tokenizer
    biobert_tokenizer_disease = pipeline("ner", model=BIOBERT_DISEASE_MODEL_NAME, tokenizer=BIOBERT_DISEASE_MODEL_NAME)
    biobert_tokenizer_chemical = pipeline("ner", model=BIOBERT_CHEMICAL_MODEL_NAME, tokenizer=BIOBERT_CHEMICAL_MODEL_NAME)

    # Initialize counters
    chemical_biobert = set()
    diseases_biobert = set()
    diseases_scispacy = set()
    chemical_scispacy = set()

    # Process the file in batches
    print('Reading file...')
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            batch = file.read(batch_size)
            if not batch:
                break  # End of file

            # Tokenize the batch            
            disease_tokens = biobert_tokenizer_disease(batch)     
            disease_tokens_biobert = [entity['word'] for entity in disease_tokens if 'DISEASE' in entity['entity'].upper()]
            diseases_biobert.update(set(disease_tokens_biobert))

            chemical_tokens = biobert_tokenizer_chemical(batch)   
            chemical_tokens_biobert = [entity['word'] for entity in chemical_tokens if 'CHEMICAL' in entity['entity'].upper()]
            chemical_biobert.update(set(chemical_tokens_biobert))
            
            doc_bc5cdr = nlp_bc5cdr(batch)
            diseases = [ent.text for ent in doc_bc5cdr.ents if ent.label_ == 'DISEASE']
            diseases_scispacy.update(set(diseases))

            chems = [ent.text for ent in doc_bc5cdr.ents if ent.label_ == 'CHEMICAL']
            chemical_scispacy.update(set(chems))

    return diseases_biobert, chemical_biobert, diseases_scispacy, chemical_scispacy

#Method calling
biobert_diseases, biobert_chemicals, scispacy_diseases, scispacy_chemicals = get_diseases_and_chemicals(READ_FILE_PATH, batch_size=10000)

# Combine arrays into a list of rows
rows = zip(list(biobert_diseases), list(biobert_chemicals), list(scispacy_diseases), list(scispacy_chemicals))

# Write the combined arrays into a CSV file
with open(WRITE_FILE_PATH, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the header row
    csv_writer.writerow(TITLES)
    
    # Write the data rows    
    for row in rows:        
        csv_writer.writerow(list(row))
        
print("Task completed")
