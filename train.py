from IO_Utils import ReadTsv
import json
import re
import sys

Vocabluary = {} # vocabluary size

# Dictionaries
messagesPerClass = {
    # "spam": 0,
    # "important": 0,
    # "promo": 0
}

sumOfWordsInClass = {
    # "spam": 0,
    # "important": 0,
    # "promo": 0
}

wordFrequencyDic = {}


def MapData(data):
    for row in data:
        # r'[^a-zA-Z ]
        # r - Raw string(makes backslashes literal, though not needed here)
        # [] - Character class(matches any single character inside the brackets)
        # ^ - Inside brackets, this means NOT(negation)
        # a - z - All lowercase letters from a to z, A - Z - All uppercase letters
        cleaned = re.sub(r'[^a-zA-Z ]+', '', row[1])
        row[1] = cleaned
        CountMessages(row)
        CountWords(row)


def CountMessages(row):
    if row[0] not in messagesPerClass:
        messagesPerClass[row[0]] = 1
    else:
        messagesPerClass[row[0]] += 1

def CountWords(row):
    words = row[1].split(' ')
    for word in words:
        if len(word) <= 2:
            continue # praleidziam iteracija jei zodis trumpesnis nei 2 raidziu
        word = word.lower()
        WordFrequency(row[0], word)
        if row[0] not in sumOfWordsInClass:
            sumOfWordsInClass[row[0]] = 1
        else:
            sumOfWordsInClass[row[0]] += 1

def WordFrequency(classType, word):
    if classType not in wordFrequencyDic:
        wordFrequencyDic[classType] = {}

    if word not in wordFrequencyDic[classType]:
            wordFrequencyDic[classType][word] = 1
            Vocabluary[word] = 1
    else:
        wordFrequencyDic[classType][word] += 1
        Vocabluary[word] = 1

def ExportToJson(filepath):

    output = {
        "messagesPerClass": messagesPerClass,
        "sumOfWordsInClass": sumOfWordsInClass,
        "wordFrequencyDic": wordFrequencyDic,
        "vocabulary length": len(Vocabluary)
    }
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(json.dumps(output, indent=3))


def ExectuteTraining(filenameData, modelJson):
    dataSet = ReadTsv(filenameData)
    MapData(dataSet)
    ExportToJson(modelJson)


trainPath = sys.argv[1]
jsonPath = sys.argv[2]
ExectuteTraining(trainPath, jsonPath)
#print(messagesPerClass)
#print(sumOfWordsInClass)
#print(wordFrequencyDic)
