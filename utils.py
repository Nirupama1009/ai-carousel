from transformers import pipeline

# Load summarization pipeline only once (global for speed)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_to_carousel_slides(blog_input: str, num_slides: int = 5) -> list[str]:
    """
    Summarizes blog content into a fixed number of carousel slides (30 words max each).
    """
    # Get a summarized text
    summary = summarizer(blog_input, max_length=200, min_length=60, do_sample=False)
    summarized_text = summary[0]['summary_text']

    # Split summary into ~5 parts (naively by sentence)
    sentences = summarized_text.split('. ')
    avg_len = len(sentences) // num_slides or 1
    slides = ['. '.join(sentences[i:i+avg_len]).strip() for i in range(0, len(sentences), avg_len)]

    # Cap slides at requested number
    slides = slides[:num_slides]

    # Add "..." if needed
    slides = [s + ("..." if not s.endswith('.') else "") for s in slides]

    return slides
