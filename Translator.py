import tkinter
from tkinter import *
from tkinter import filedialog
import TranslateFunc
import tkinter.font as font

window = Tk()
window.resizable(False,False)
window.title("Morse Translator")
mainFrame = Frame(window, width=400)
mainFrame.pack()

filePath = ""
radioChoose = IntVar()
savePath = ""

titleFont = font.Font(family="Helvtica", size=30)
infoFont = font.Font(family="Helvtica", size=15)

chooseFileButton = Button(window, text="Choose File to Translate")
saveFolderButton = Button(window, text="Choose Folder to Save")
filePathLabel = Label(window, text="")
folderPathLabel = Label(window, text="")
errorLabel = Label(window, text="")

def chooseFile():
    global filePath
    filePath = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    if filePath != "":
        chooseFileButton.config(text="Change File")
        filePathLabel.config(text=filePath)

def chooseFolder():
    global savePath
    savePath = filedialog.askdirectory()
    if savePath != "":
        saveFolderButton.config(text="Change Folder")
        folderPathLabel.config(text=savePath)

def continueTrans():
    if filePath == "" or savePath == "":
        errorLabel.config(text="Please Choose File")
    else:
        TranslateFunc.Translate(filePath,radioChoose.get(),savePath)
        errorLabel.config(text="File Created!")

titleLabel = Label(window, text="Morse Translator",font=titleFont,height=2).pack()

infoLabel = Label(window, text="Choose file to translate, pick from which language,\n and where to save it, and get your translate\n file to your computer.", font=infoFont).pack()

space = Label(window, text="",height=0).pack()

filePathLabel.pack()

chooseFileButton.config(command=chooseFile)
chooseFileButton.pack()

space = Label(window, text="",height=0).pack()

radioButton = Radiobutton(window, text="English To Morse",padx = 20, variable=radioChoose,value=0).pack()
radioButton = Radiobutton(window, text="Morse To English",padx = 20, variable=radioChoose,value=1).pack()

space = Label(window, text="",height=2).pack()

folderPathLabel.pack()

saveFolderButton.config(command=chooseFolder)
saveFolderButton.pack()

space = Label(window, text="",height=2).pack()

errorLabel.pack()

startTranslateButton = Button(window,text="Start Translate", command=continueTrans).pack()

space = Label(window, text="",height=3).pack()

creditLabel = Label(window, text="Made By Ofek Grego").pack()

window.mainloop()
