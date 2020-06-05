import tkinter
from tkinter import *
from tkinter import filedialog

window = Tk()
window.resizable(False,False)
window.title("Morse Translator")
mainFrame = Frame(window, width=400)
mainFrame.pack()

filePath = ""
radioChoose = IntVar()

chooseFileButton = Button(window, text="Choose File to Translate")
filePathLabel = Label(window, text="")

def ShowChoice():
    print(radioChoose.get())

def chooseFile():
    global filePath
    filePath = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filePath)
    if filePath != "":
        chooseFileButton.config(text="Change File")
        filePathLabel.config(text="File Path: " + filePath)

space = Label(window, text="",height=2).pack()

titleLabel = Label(window, text="Morse Translator").pack()

space = Label(window, text="",height=3).pack()

filePathLabel.pack()

chooseFileButton.config(command=chooseFile)
chooseFileButton.pack()

space = Label(window, text="",height=0).pack()

radioButton = Radiobutton(window, text="English To Morse",padx = 20, variable=radioChoose, command=ShowChoice,value=0).pack()
radioButton = Radiobutton(window, text="Morse To English",padx = 20, variable=radioChoose, command=ShowChoice,value=1).pack()

space = Label(window, text="",height=3).pack()

startTranslateButton = Button(window,text="Start Translate").pack()

space = Label(window, text="",height=3).pack()

creditLabel = Label(window, text="Made By Ofek Grego").pack()

window.mainloop()
