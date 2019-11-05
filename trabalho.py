import copy

def appStart():
    fileName = getFileName()
    fileStopwordsName = getFileStopwordsName()
    stopWordsFile = openFile(fileStopwordsName)
    generalFile = openFile(fileName)
    print(showWords(generalFile, stopWordsFile))
    stopWordsFile.close()
    generalFile.close()
    stopWordsFile = openFile(fileStopwordsName)
    generalFile = openFile(fileName)
    print(moreWords(showWords(generalFile, stopWordsFile)))
    stopWordsFile.close()
    generalFile.close()


def getFileName():
    return input("Entre com o nome do arquivo: ")

def getFileStopwordsName():
    return input("Entre com o nome do arquivo com as palavras a serem ignoradas: ")

def openFile(fileName):
    return open(fileName, 'r', encoding="UTF-8")

def moreWords(wordsDictonary):
    newDictonary = copy.deepcopy(wordsDictonary)
    maispresente = 0
    wordsMoreUsed = {}
    for i in newDictonary:
        if newDictonary[i] > maispresente:
            maispresente = newDictonary[i]
    for i in newDictonary:
        if(newDictonary[i] == maispresente):
            wordsMoreUsed[i] = maispresente
    return wordsMoreUsed

def showWords(generalFile, stopWordsFile):
    wordsDictonary = {}
    ignoredWords = []
    for ignored in stopWordsFile:
        ignored = ignored.replace("\n", "")
        ignoredWords.append(ignored)
    for word in generalFile:
        word = word.replace("\n", "")
        if(word not in ignoredWords):
            if(word in wordsDictonary):
                qtde = wordsDictonary[word]
                wordsDictonary[word] = (wordsDictonary[word] + 1)
            else:
                wordsDictonary[word] = 1
    return wordsDictonary

appStart()