
englishArray = ["A","B","C","D","E","F","G","H","I","J","K",
            "L","M","N","O","P","Q","R","S","T",
            "U","V","X","W","Y","Z",",",".","\n"," ",""]
morseArray = [".-","-...","-.-.","-..",".","..-.","--.","....",
            "..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...",
            "-","..-","...-",".--","-..-","-.--","--..",",",".","\n"," ",""]

def Translate(filePath, EnglishMorse):
    # print(filePath)
    # print(EnglishMorse)
    endText = ""
    fileText = open(filePath, "r").read()
    if EnglishMorse == 0:
        for i in range(len(fileText)):
            endText += morseArray[englishArray.index(str(fileText[i]).upper())] + " "
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

    print(endText)
