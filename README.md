<img width="1920" height="1080" alt="Screenshot 2025-07-11 210956" src="https://github.com/user-attachments/assets/ba8a30de-51c9-4745-b7b4-5ac4e344e781" />
<img width="1920" height="1080" alt="Screenshot 2025-07-11 211113" src="https://github.com/user-attachments/assets/c3049061-78d0-48de-8d6c-c3eb835f5954" />
<img width="1920" height="1080" alt="Screenshot 2025-07-11 211134" src="https://github.com/user-attachments/assets/c1fee4de-ed91-4938-9922-c76a4ef32b24" />
<img width="1920" height="1080" alt="Screenshot 2025-07-11 211154" src="https://github.com/user-attachments/assets/6c5dc37b-e8a2-423f-8127-c74ffc1b0c16" />
# AI Carousel Generator :

Turn your blog posts into eye-catching, Instagram-style carousels in seconds.

📝 → 🔍 → 🎠 → 📄
Blog → AI Summary → Swipeable Slides → Download as PDF

---

* Features :

✅ FastAPI backend
✅ Text-to-slide carousel generation
✅ Swiper.js integration for real Instagram feel
✅ PDF export using wkhtmltopdf
✅ Mobile-friendly, clean UI
✅ Easy to extend with PNG export, login & more

---

* Tech Stack :

- Python + FastAPI

- HTML + Jinja2 Templates

- Swiper.js (JS-based carousel)

- CSS (custom + swiper-bundle.min.css)

- pdfkit + wkhtmltopdf (for PDF generation)

---

📂 Folder Structure

ai_carousel/
├── main.py
├── templates/
│   ├── form.html
│   └── carousel.html
├── static/
│   ├── styles.css
│   ├── swiper-bundle.min.css
│   └── swiper-bundle.min.js
├── generated_pdfs/
├── requirements.txt
└── README.md

---

*  How to Run Locally :

1. Clone this repo:
     git clone https://github.com/yourusername/ai_carousel.git
     cd ai_carousel

2. Create a virtual environment:
     python -m venv venv
     .\venv\Scripts\activate

3. Install dependencies:
    pip install -r requirements.txt

4. Install wkhtmltopdf (Windows):
     - Download: https://wkhtmltopdf.org/downloads.html
     - Install it
     - Update this path in main.py:
 # code :
   path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

5. Run the app:
    uvicorn main:app --reload 

6. Open your browser :

    http://localhost:8000


*  Future Features :

- [ ] Download each slide as PNG

- [ ] Instagram Auto-Post via Meta API

- [ ] User login & saved history

- [ ] Theme customization (fonts, emojis, colors)

- [ ] Chrome Extension for blog import

