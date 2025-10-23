import pyttsx3
from PyPDF2 import PdfReader

pdf = open("sample.pdf", 'rb')     # first parameter is the name of the PDF file
pdf_reader = PdfReader(pdf) 

print("Welcome to Text-To-Speech!")
text_to_speech = pyttsx3.init()

read_more_pages = True
while read_more_pages:
    print("Ex: To read a specific page, enter the current page number (in the PDF reader, not the actual PDF) and subtract one.\n")
    while True:
        try:
            page_num = int(input("Enter page number: "))
            if 0 <= page_num < len(pdf_reader.pages):
                break
            else:
                print("Please enter a valid integer!\n")
        except ValueError:
            print("Invalid input! Please enter a valid integer!\n")

    page_to_read = pdf_reader.pages[page_num]

    text = page_to_read.extract_text()
    text_to_speech.say(text)
    text_to_speech.runAndWait()
    
    answer = input("Would you like to read more pages? Enter 'YES' to continue: \n")
    if answer != "YES":
        read_more_pages = False

print("Thank you for using Text-To-Speech!\n")
pdf.close()    # closes the PdfReader object