import torch
from transformers import AutoModel
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load pre-trained model
model = AutoModel.from_pretrained("bert-base-uncased")

# Convert tokens to tensor
input_ids = torch.tensor([tokenizer.convert_tokens_to_ids(tokens)])

# Get hidden states (embeddings)
with torch.no_grad():
    outputs = model(input_ids)
    embeddings = outputs.last_hidden_state.squeeze().numpy()

# Reduce dimensions using PCA
pca = PCA(n_components=2)
reduced_embeddings = pca.fit_transform(embeddings)

# Plot embeddings
plt.figure(figsize=(8,6))
plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], color='blue')

for i, token in enumerate(tokens):
    plt.text(reduced_embeddings[i, 0], reduced_embeddings[i, 1], token, fontsize=12)

plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("Token Embeddings Visualization")
plt.show()
