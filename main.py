from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfReader
from PIL import ImageTk, Image
import docx2txt
import pyttsx3 

window = Tk()
window.title("Audiobook")
window.geometry("600x400")

def read_pdf(file):
    reader = PdfReader(file)
    all_pages = []
    for page in reader.pages:
        all_pages.append(page.extract_text())
    return all_pages


def read_word(file):
    content = docx2txt.process(file)
    return content


def audiobook(file):
    file_extension = file.split('.')[-1].lower()
    if file_extension == 'pdf':
        text = read_pdf(file)
    elif file_extension == 'docx':
        text = read_word(file)
    else:
        messagebox.showerror(title="Stop human", message="Ouch, can't read that file")
        return
    
    engine = pyttsx3.init()
    engine.save_to_file('\n'.join(text),"audio_file.mp3")
    engine.runAndWait()
    messagebox.showinfo(title="Success", message="Audiobook generated successfully!")
    
    
def upload_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("PDF Files", "*.pdf"), ("Word Files", "*.docx")])
    if file_path:
        print("Selected file:", file_path)
        audiobook(file_path)
    
    
image1 = Image.open("/home/maggie/Documents/Portafolio/pdf to audiobook/images/foto.png")
test = ImageTk.PhotoImage(image1)
label1 = Label(window,image=test)
label1.image = test
label1.place(x=0, y=0)

text = Label(window,text="Convert a file into an audiobook")
text.configure(bg="#FFF3E2",font=("Helvetica",22, "bold"))
text.place(x=80,y=120)

text2 = Label(window,text="Only Pdf and Word files allowed!")
text2.configure(bg="#FFF3E2",font=("Helvetica",14))
text2.place(x=170,y=150)

user_img = Button(window, text="Get File", width=8, height=1,font=("Helvetica",14),bg="#FFF3E2", command=upload_file)
user_img.place(x=250,y=220)


window.mainloop()   
    
    
    
    