import sys
import argparse
import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_information(text):
    patterns = {
        'Email': re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b', re.IGNORECASE),
        'Phone': re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'),
        'Skills': re.compile(r'\bSkills\b.*?:(.*?)(?:\n\n|\Z)', re.IGNORECASE | re.DOTALL),
        'Education': re.compile(r'\b(?:Education|University|College)\b(.*?)(?:\n\n|\Z)', re.IGNORECASE | re.DOTALL),
        'Experience': re.compile(r'\b(?:Experience|Employment|Professional History|Work Experience)\b(.*?)(?:\n\n|\Z)', re.IGNORECASE | re.DOTALL),
        'Certifications': re.compile(r'\b(Certifications)\b(.*?)(?:\n\n|\Z)', re.IGNORECASE | re.DOTALL)
    }

    extracted_info = {}
    for key, regex in patterns.items():
        matches = re.findall(regex, text)
        extracted_info[key] = ' '.join([' '.join(match) for match in matches]).strip() if matches else "Not Found"

    return extracted_info

def main():
    parser = argparse.ArgumentParser(description="Extract resume details similar to ATS processing and display full text.")
    parser.add_argument('resume', type=str, help='The file path to the resume PDF.')
    args = parser.parse_args()

    text = extract_text_from_pdf(args.resume)
    if text:
        print("\nFull Text Extracted from Resume:\n")
        print(text)
        print("\nExtracted Information for ATS System:\n")
        information = extract_information(text)
        for key, value in information.items():
            print(f"{key}: {value}\n")
    else:
        print("Failed to extract text from the PDF.")

if __name__ == "__main__":
    main()
