from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pdfkit
import os
import uuid

app = FastAPI()

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Template directory
templates = Jinja2Templates(directory="templates")

# Path to wkhtmltopdf executable
path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
pdf_config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, blog_input: str = Form(...)):
    slides = [s.strip() for s in blog_input.split('.') if s.strip()]
    slides = slides[:10]  # Limit number of slides

    # Create PDF from blog input
    pdf_html = "<br><br>".join(slides)
    full_html = f"<html><body><h1>Blog Summary</h1><p>{pdf_html}</p></body></html>"

    filename = f"{uuid.uuid4()}.pdf"
    pdf_path = os.path.join("static", filename)
    pdfkit.from_string(full_html, pdf_path, configuration=pdf_config)

    return templates.TemplateResponse("carousel.html", {
        "request": request,
        "slides": slides,
        "filename": filename
    })

@app.get("/download/{filename}")
async def download_pdf(filename: str):
    file_path = os.path.join("static", filename)
    return FileResponse(file_path, media_type='application/pdf', filename="blog_summary.pdf")