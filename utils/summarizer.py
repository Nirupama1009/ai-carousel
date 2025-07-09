from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_blog(text):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summary = ""
    for chunk in chunks:
        result = summarizer(chunk, max_length=100, min_length=30, do_sample=False)
        summary += result[0]["summary_text"] + " "
    return summary.strip()
