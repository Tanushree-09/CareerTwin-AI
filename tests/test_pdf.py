from app.services.pdf_service import PDFService

pdf = PDFService()

text = pdf.extract_text("resume.pdf")

print(text)