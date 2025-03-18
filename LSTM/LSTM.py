import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding

# Sample text dataset
text = "This is a simple text generation example using LSTMs. LSTMs can generate sequential text." * 10

# Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
vocab_size = len(tokenizer.word_index) + 1

# Convert text to sequences
input_sequences = []
words = text.split()
for i in range(1, len(words)):
    sequence = words[:i+1]
    encoded_sequence = tokenizer.texts_to_sequences([sequence])[0]
    input_sequences.append(encoded_sequence)

# Pad sequences
max_length = max(len(seq) for seq in input_sequences)
input_sequences = pad_sequences(input_sequences, maxlen=max_length, padding='pre')

# Split into features and labels
X, y = input_sequences[:, :-1], input_sequences[:, -1]
y = tf.keras.utils.to_categorical(y, num_classes=vocab_size)

# Build the LSTM model
model = Sequential([
    Embedding(vocab_size, 50, input_length=max_length-1),
    LSTM(100, return_sequences=True),
    LSTM(100),
    Dense(100, activation='relu'),
    Dense(vocab_size, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=50, verbose=1)

# Function to generate text
def generate_text(seed_text, next_words, model, max_length):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_length-1, padding='pre')
        predicted = np.argmax(model.predict(token_list, verbose=0), axis=-1)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text

# Generate new text
print(generate_text("This is", 10, model, max_length))
