import fitz  # PyMuPDF
import re
import json

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def parse_resume(resume_text):
    # Define patterns for sections
    sections = {
        "contact_information": r"Contact Information\n(.*?)\n\n",
        "education": r"Education\n(.*?)\n\n",
        "work_experience": r"Work Experience\n(.*?)\n\n",
        "skills": r"Skills\n(.*?)\n\n",
        "projects": r"Projects\n(.*?)\n\n"
    }

    # Initialize result dictionary
    parsed_resume = {}

    # Extract sections using regex
    for section, pattern in sections.items():
        match = re.search(pattern, resume_text, re.DOTALL)
        if match:
            parsed_resume[section] = match.group(1).strip()

    return json.dumps(parsed_resume, indent=4)

# Example usage
pdf_path = "path/to/your/resume.pdf"  # Replace with your PDF file path
resume_text = extract_text_from_pdf(pdf_path)
parsed_resume = parse_resume(resume_text)
print(parsed_resume)
