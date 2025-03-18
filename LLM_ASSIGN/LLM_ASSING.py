from transformers import AutoTokenizer  
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")  
text = "Your sample text here."  
tokens = tokenizer.tokenize(text)  
print(tokens, len(tokens))  

from transformers import AutoModel  
model = AutoModel.from_pretrained("bert-base-uncased")  
embeddings = model(**tokenizer(text, return_tensors="pt"))  
