import pyttsx3  #first we need to import packages i.e pyttsx3[python text to speech version 3] and PyPDF[python PDF version 2]
import PyPDF2

book= open('python.pdf', 'rb')                       # 'rb':read as binary              
pdfReader = PyPDF2.PdfReader(book)

page = pdfReader._get_num_pages()                    # to count how many pages are there in pdf

print(page)
speaker = pyttsx3.init()

page = pdfReader._get_page(8)                        #to start reading from page number 8
text = page.extract_text()                           #to extract the text



speaker.say(text)                                    #to make speaker work


speaker.runAndWait()