def generate_slides(summary):
    sentences = summary.split(". ")
    slides = []
    slide = ""
    for sentence in sentences:
        if len(slide + sentence) < 300:
            slide += sentence + ". "
        else:
            slides.append(slide.strip())
            slide = sentence + ". "
    if slide:
        slides.append(slide.strip())
    return slides
