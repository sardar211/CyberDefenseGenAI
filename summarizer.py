from transformers import pipeline

# Load summarizer
summarizer = pipeline("summarization")

# Load input from file
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Perform summarization
summary = summarizer(text, max_length=150, min_length=30, do_sample=False)

# Save summary to file
with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(summary[0]['summary_text'])

print("✅ Summary saved to summary.txt")
