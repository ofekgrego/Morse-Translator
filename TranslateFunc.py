
englishArray = ["A","B","C","D","E","F","G","H","I","J","K",
            "L","M","N","O","P","Q","R","S","T",
            "U","V","X","W","Y","Z","0","1","2","3","4","5","6","7","8","9"
            ",",".","\n"," ",""]
morseArray = [".-","-...","-.-.","-..",".","..-.","--.","....",
            "..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...",
            "-","..-","...-",".--","-..-","-.--","--..","-----",".----","..---","...--",
            "....-",".....","-....","--...","---..","----."
            ",",".","\n"," ",""]

def Translate(filePath, EnglishMorse,savePath):
    fileSplit = savePath.split("/")
    filePathSplit = filePath.split("/")
    fileName = filePathSplit[len(filePathSplit)-1].split(".")[0]
    print(fileName)

    endText = ""
    fileText = open(filePath, "r").read()
    if EnglishMorse == 0:
        for i in range(len(fileText)):
            endText += morseArray[englishArray.index(str(fileText[i]).upper())] + " "
            newFile = open(savePath+"/"+fileName+"ToMorse.txt","w+")
    else:
        group = ""
        spaceCount = 0
        for i in range(len(fileText)):
            if fileText[i] == "\n":
                endText += englishArray[morseArray.index(str(group))].lower()
                group = ""
                endText += fileText[i]
            else:
                if fileText[i] != " ":
                    group += fileText[i]
                    spaceCount = 0
                else:
                    # print(group)
                    if spaceCount <= 1:
                        endText += englishArray[morseArray.index(str(group))].lower()
                        group = ""
                    else:
                        endText += " "
                    spaceCount += 1
        newFile = open(savePath+"/"+fileName+"ToEngish.txt","w+")

    newFile.write(endText)
    newFile.close()
