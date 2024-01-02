from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
model = AutoModel.from_pretrained('bert-base-uncased')
files = ['ALLTEXT.txt']
inputs = tokenizer(files, return_tensors='pt')
outputs = model(**inputs)