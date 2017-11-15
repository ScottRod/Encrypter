import random
import os.path
# this can be changed by the user

version = "1.0"

AlphaBet = ["?","!","\n","u","7","@","(",",","9",")", ".","+",":"," ","a","8","-", "b","n","j","e", "f", "g","/", "h", "i","4", "k","0","w", "l",";","2", "m","d","5", "o","=", "p","3","6", "q","z","x", "t", "v" ,"s","c", "y","r", "1"]

EncyptionMethods = ["!","@"]

def ReadFile(openAs):
    newFile = open(input("File to Open: "), openAs)
    print(newFile.read())
    newFile.close()

def WriteFile(openAs, words, file):
    File = open(file, openAs)
    File.write(words)

def Key():
    print("Current Encryption Symbol List")
    for x in AlphaBet:
        if x == "\n":
            x = "\\n"
        if x == " ":
            x = "space"
        print(x)

def Tutorial():
    print("All of the commands that can be done on the ui's can also be done in text")
    print("The functions are Encrypt(method, fileToEncrypt)")
    print("for what methods you have downloaded type in Info()")
    print("Decrypt(words)")
    print("copy and paste the encrypted words in between the brackets to decypt them")
    print("Example of Encrypting")
    print("Encrypt(2, '/Desktop/example.txt')")
    print("Example of Decrypting")
    print("Decrypt('@__-704__v900__n828__+484__4650__4468__m726')")
    print("To update the encyrption method either do it in the ui's or in the txt file")
    print("make sure you include all of the symbols")

def Info():
    print("Version: "+version)
    print("Downloaded Encryption Methods")
    counter = 0
    for x in EncyptionMethods:
        print(x,counter+1)
        counter += 1
    print("For more encryption methods visit ...")
    print("Look out for the next update on ....")

# converts the file to binary

def STBF(fileToConvert):
    FTC = open(fileToConvert, "r")
    NBF = open(fileToConvert+".bin", "wb")
    for x in FTC.read():
        x = x.lower()
        if x == "a":
            NBF.write(b'a')
        if x == "b":
            NBF.write(b'b')
        if x == "c":
            NBF.write(b'c')
        if x == "d":
            NBF.write(b'd')
        if x == "e":
            NBF.write(b'e')
        if x == "f":
            NBF.write(b'f')
        if x == "g":
            NBF.write(b'g')
        if x == "h":
            NBF.write(b'h')
        if x == "i":
            NBF.write(b'i')
        if x == "j":
            NBF.write(b'j')
        if x == "k":
            NBF.write(b'k')
        if x == "l":
            NBF.write(b'l')
        if x == "m":
            NBF.write(b'm')
        if x == "n":
            NBF.write(b'n')
        if x == "o":
            NBF.write(b'o')
        if x == "p":
            NBF.write(b'p')
        if x == "q":
            NBF.write(b'q')
        if x == "r":
            NBF.write(b'r')
        if x == "s":
            NBF.write(b's')
        if x == "t":
            NBF.write(b't')
        if x == "v":
            NBF.write(b'v')
        if x == "u":
            NBF.write(b'u')
        if x == "w":
            NBF.write(b'w')
        if x == "x":
            NBF.write(b'x')
        if x == "y":
            NBF.write(b'y')
        if x == "z":
            NBF.write(b'z')
        if x == " ":
            NBF.write(b' ')
    FTC.close()
    NBF.close()

def CheckIfNum(x):
    for y in range(10):
        if x == str(y):
            return True
    return False

def WithInBoundries(value,x,y):
    if value > x and value < y:
        return True
    else:
        return False

def Encrypt(method, file):
    if os.path.isfile(file):
        if method == 1:
            IN = file
            File = open(IN, "r")
            ReadFile = File.read()
            File.close()
            newFile = open(IN, "w")
            newFile.write("!")
            for x in ReadFile:
                x = x.lower()
                x = AlphaBet.index(x)
                if x > 9:
                    newFile.write("_")
                newFile.write(str(int(x)))
            newFile.close()
        if method == 2:
            IN = file
            File = open(IN, "r")
            ReadFile = File.read()
            File.close()
            newFile = open(IN, "w")
            newFile.write("@")
            for x in ReadFile:
                x = x.lower()
                x = AlphaBet.index(x)
                y = random.randint(1,len(AlphaBet)-1)
                if x*y > 9:
                    newFile.write("_")
                if x*y > 99:
                    newFile.write("_")
                if x*y > 999:
                    newFile.write("_")
                if x*y > 9999:
                    newFile.write("_")
                newFile.write(AlphaBet[y])
                newFile.write(str(int(x)*y))
            newFile.close()
    else:
        print("The file given doesn't exist, please check the directory")

def Decrypt(words):
    method = 0
    strX = words
    counter = 0
    outputStr = ""
    for x in strX:
        if counter == 0 and x == "!":
            method = 1
            counter += 1 
        if counter == 0 and x == "@":
            method = 2
            counter += 1
        if method == 1:
            if counter < len(strX):
                x = strX[counter]
            if x == "_" and counter < len(strX):
                x = strX[int(counter)+1] + strX[int(counter)+2]
                counter += 2
            if x != "_":
                x = AlphaBet[int(x)]
                counter += 1
            if counter < len(strX):
                outputStr = outputStr + x
        if method == 2:
            if counter < len(strX):
                x = strX[counter]
            y = False
            if x == "_" and counter < len(strX):
                if strX[counter+1] == "_" and strX[counter+2] == "_" and strX[counter+3] == "_" and y == False and counter + 9 < len(strX):
                    z = AlphaBet.index(strX[counter+4])
                    x = strX[counter+5] + strX[counter+6] + strX[counter+7] + strX[counter+8] + strX[counter+9]
                    x = str(int(x) / z)
                    outputStr = outputStr + AlphaBet[int(float(x))]
                    counter += 6
                    y = True
                if strX[counter+1] == "_" and strX[counter+2] == "_" and y == False and counter + 7 < len(strX):
                    z = AlphaBet.index(strX[counter+3])
                    x = strX[counter+4] + strX[counter+5] + strX[counter+6] + strX[counter+7]
                    x = str(int(x) / z)
                    outputStr = outputStr + AlphaBet[int(float(x))]
                    counter += 5
                    y = True
                if strX[counter+1] == "_" and y == False and counter + 5 < len(strX):
                    z = AlphaBet.index(strX[counter+2])
                    x = strX[counter+3] + strX[counter+4] + strX[counter+5]
                    x = str(int(x) / z)
                    outputStr = outputStr + AlphaBet[int(float(x))]
                    counter += 4
                    y = True
                if strX[counter+1] != "_" and counter + 3 < len(strX) and y == False:
                    z = AlphaBet.index(strX[counter+1])
                    x = strX[counter+2] + strX[counter+3]
                    x = str(int(x) / z)
                    outputStr = outputStr + AlphaBet[int(float(x))]
                    counter += 3
                    y = True
                    outputStr = outputStr + AlphaBet[int(float(x))]
            if counter + 1 < len(strX) and y == False and CheckIfNum(strX[counter+1]) and not CheckIfNum(x):
                if x != "_" and counter < len(strX) and y == False:
                    z = AlphaBet.index(strX[counter])
                    x = str(int(strX[counter+1]) / z)
                    counter += 2
                    y = True
                    outputStr = outputStr + AlphaBet[int(float(x))]
            counter += 1
    return outputStr


import math

import tkinter as tk

class vec2():
    def init(self,x,y):
        self.x = x
        self.y = y
        self.w = x
        self.h = y

def createWindow(title,minsize,maxsize):
    if minsize.x >= maxsize.x:
        maxsize.x = minsize.x + 20
    if minsize.y >= maxsize.y:
        maxsize.y = minsize.y + 20
    root = tk.Tk()
    root.title(title)
    root.minsize(width=minsize.x,height=minsize.y)
    root.maxsize(width=maxsize.x,height=maxsize.y)
    return root

def createLabel(root,text,font):
    label = tk.Label(root,text=text,font=font)
    return label

def createEntry(root):
    entry = tk.Entry(root)
    return entry



minsize = vec2()

minsize.init(300,300)

maxsize = vec2()

maxsize.init(700,700)

mainWindow = createWindow("Encryption",minsize,maxsize)

Title = createLabel(mainWindow,"Encryption","copperplate")

Title.pack()

WayToEncryptLabel = createLabel(mainWindow, "Level of Encryption: ", "copperplate")

WayToEncryptLabel.pack()

WayToEncrypt = createEntry(mainWindow)

WayToEncrypt.pack()

FileToEncryptLabel = createLabel(mainWindow, "File: ", "copperplate")

FileToEncryptLabel.pack()

FileToEncrypt = createEntry(mainWindow)

FileToEncrypt.pack()


def EncryptClick():
    Encrypt(int(WayToEncrypt.get()), FileToEncrypt.get())
    y = createLabel(mainWindow, "Encrypted Successfully", "copperplate")
    y.pack()

def createButton(root, text, callback):
    button = tk.Button(root, text=text, command=callback)
    return button

EncryptButton = createButton(mainWindow, "Encrypt", EncryptClick)

EncryptButton.pack()

DecryptLabel = createLabel(mainWindow, "Encrypted text: ", "copperplate")

DecryptLabel.pack()

DecryptEntry = createEntry(mainWindow)

DecryptEntry.pack()

def DecryptClick():
    x = Decrypt(DecryptEntry.get())
    WriteFile("w", x, FileToEncrypt.get())
    y = createLabel(mainWindow, "Decrypted Successfully", "copperplate")
    y.pack()

DecryptButton = createButton(mainWindow, "Decrypt", DecryptClick)

DecryptButton.pack()

minsize = vec2()

minsize.init(250,1000)

maxsize = vec2()

maxsize.init(2000,2000)

AlphaBetWindow = createWindow("Encode", minsize,maxsize)

AlphaBetWindow2 = createWindow("Encode 2", minsize,maxsize)

AlphaBetWindow3 = createWindow("Encode 3", minsize,maxsize)

AlphaBetWindow4 = createWindow("Encode 4", minsize,maxsize)

TitleAlphaBet = createLabel(AlphaBetWindow, "Encode", "copperplate")

TitleAlphaBet.pack()

TitleAlphaBet2 = createLabel(AlphaBetWindow2, "Encode 2", "copperplate")

TitleAlphaBet2.pack()

TitleAlphaBet3 = createLabel(AlphaBetWindow3, "Encode 3", "copperplate")

TitleAlphaBet3.pack()

def UpdateAlphaBet():
    for x in EncodeEntries:
        AlphaBet[EncodeEntries.index(x)] = x.get()
    y = createLabel(TitleAlphaBet3, "Updated encryption successfully", "copperplate")
    if os.path.isfile("/users/scottblyth/Desktop/Current Encryption Key.txt"):
        file = open("/users/scottblyth/Desktop/Current Encryption Key.txt", "w")
        for x in AlphaBet:
            file.write(x)

UpdateEncode = createButton(TitleAlphaBet3, "Update Encryption", UpdateAlphaBet)

UpdateEncode.pack()

print("Type in Key() for the current setup of the encryption key")

print("Type in Tutorial() for information on how to use this programme")

print("Type in Info() to get your current version and where to get updates")

print("Note: before doing all this close all windows excluding this one")

if not os.path.isfile("/users/scottblyth/Desktop/Current Encryption Key.txt"):
    random.shuffle(AlphaBet)
    file = open("/users/scottblyth/Desktop/Current Encryption Key.txt", "w")
    for x in AlphaBet:
        file.write(x)
    file.close()
else:
    file = open("/users/scottblyth/Desktop/Current Encryption Key.txt", "r")
    strX = file.read()
    counter = 0
    for x in strX:
        AlphaBet[counter] = x
        counter += 1
    file.close()

EncodeEntries = []

EncodeNumbers = []

for x in range(len(AlphaBet)):
    if x < 14:
        EncodeNumbers.insert(x,createLabel(AlphaBetWindow, str(x+1), "copperplate"))
        EncodeEntries.insert(x, createEntry(AlphaBetWindow))
        EncodeEntries[x].insert(x, AlphaBet[x])
    if x >= 14 and x < 14*2:
        EncodeNumbers.insert(x,createLabel(AlphaBetWindow2, str(x+1), "copperplate"))
        EncodeEntries.insert(x, createEntry(AlphaBetWindow2))
        EncodeEntries[x].insert(x, AlphaBet[x])
    if x >= 14*2 and x < 14*3:
        EncodeNumbers.insert(x,createLabel(AlphaBetWindow3, str(x+1), "copperplate"))
        EncodeEntries.insert(x, createEntry(AlphaBetWindow3))
        EncodeEntries[x].insert(x, AlphaBet[x])
    if x >= 14*3 and x < 14*4:
        EncodeNumbers.insert(x,createLabel(AlphaBetWindow4, str(x+1), "copperplate"))
        EncodeEntries.insert(x, createEntry(AlphaBetWindow4))
        EncodeEntries[x].insert(x, AlphaBet[x])

for x in EncodeEntries:
    EncodeNumbers[EncodeEntries.index(x)].pack()
    x.pack()

def Shuffle():
    random.shuffle(AlphaBet)
    print("The file is a txt file")
    x = input("File to store new encryption in: ")
    print("New Symbols order")
    file = open(x+".txt", "w")
    for x in AlphaBet:
        print(x)
        file.write(x)
    file.close()

def Change(file):
    keyfile = open(file,"r")
    strX = keyfile.read()
    for x in strX:
        AlphaBet[strX.index(x)] = x
    keyfile.close()
    print("Using Encryption Key: ")
    for x in AlphaBet:
        print(x)
    

AlphaBetWindow.mainloop()
AlphaBetWindow2.mainloop()
AlphaBetWindow3.mainloop()
AlphaBetWindow4.mainloop()
mainWindow.mainloop()
