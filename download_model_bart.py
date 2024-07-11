from transformers import pipeline

# Download the model files
pipe = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
pipe.save_pretrained("./local-bart-large-mnli")