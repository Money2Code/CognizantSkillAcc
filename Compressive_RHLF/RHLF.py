import torch
from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments, AutoTokenizer
from datasets import Dataset

# Load pre-trained model and tokenizer
model_name = "distilbert-base-uncased"
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Sample feedback dataset
feedback_data = {
    "text": [
        "Frequent headaches can be caused by stress, dehydration, or medical conditions. Maintain hydration and consult a doctor.",
        "Drink water and rest. Visit a doctor if it doesn’t improve.",
        "Take two painkillers every 4 hours."
    ],
    "label": [2, 1, 0]  # Higher score = better response
}

# Convert to Hugging Face dataset format
dataset = Dataset.from_dict(feedback_data)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./rlhf_model",
    per_device_train_batch_size=8,
    num_train_epochs=3,
    evaluation_strategy="epoch",
)

# Train RLHF reward model
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

trainer.train()

# Save fine-tuned model
model.save_pretrained("./fine_tuned_healthbot")
tokenizer.save_pretrained("./fine_tuned_healthbot")
