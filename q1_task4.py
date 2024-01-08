currently working on this

import spacy
from spacy import displacy 
from transformers import BertTokenizer, BertForTokenClassification

#Establisng spacy models
nlp_bc5cdr_md=spacy.load('en_ner_bc5cdr_md')
nlp_sci_sm=spacy.load('en_core_sci_sm')
