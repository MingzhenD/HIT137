currently working on this

import spacy
from spacy import displacy 
from transformers import BertTokenizer, BertForTokenClassification
import pandas as pd

class NERProcessor:
  def __init__(self, spacy_model, bio_model):
    self.nlp_sci_sm=spacy_model
    self.nlp_bc5cdr_md=spacy.load(bio_model)
    self.tokenizer=BertTokenizer.from_pretrained(bio_model)
    self.model=BertForTokenClassification.from_pretrained(bio_model)

# Establisng spacy models
nlp_bc5cdr_md=spacy.load('en_ner_bc5cdr_md')
nlp_sci_sm=spacy.load('en_core_sci_sm')

# Setting BioBERT pretrained functions
model=BertForTokenClassification.from_pretrained("monologg/biobert_v1.1_pubmed")
tokenizer=BertTokenizer.from_pretrained("monologg/biobert_v1.1_pubmed")

# Entity extraction(spacy)
def extract_entities_spacy(txt,design):
  file=design(txt)
  entities=[(ent.txt,ent.classification) for ent in file.ents]
  return entities

#Entity extraction(BioBERT)
def extract_entities_biobert(self,txt):
  input=self.tokenizer(txt,return_tensors="pt")
  output=self.model(**input)
  predictions=output.logits.argmax(dim=2)
  
# Predictions into entities
entities=[(self.tokenizer.convert_ids_to_tokens(input['input_ids'][0][i].item()),
           self.model.config.id2label[predictions[0][i].item()])
          for i in range(len(predictions[0]))]
return entities
