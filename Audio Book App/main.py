import pyttsx3
import PyPDF2


files = open("text.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(files)
pages = pdfReader.numPages
print(pages)
Speak = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(7)
    text = page.extractText()
    Speak.say(text)
    Speak.runAndWait()
