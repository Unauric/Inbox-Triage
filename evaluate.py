import sys
from nb_model import NaiveBayesModel
from IO_Utils import ReadTsv

modelPath = sys.argv[1]
testPath = sys.argv[2]

a = NaiveBayesModel.from_dict(modelPath)
dataSet = ReadTsv(testPath)
confusionMatrix = {
    "important" : {"important": 0, "promo": 0, "spam": 0},
    "promo" : {"important": 0, "promo": 0, "spam": 0},
    "spam": {"important": 0, "promo": 0, "spam": 0},

}

for row in dataSet:
    predicted_label, scores = a.Predict(row[1])
    #print(row)
    #print(predicted_label, scores)
    #print()
    if predicted_label == row[0]:
        confusionMatrix[row[0]][predicted_label] += 1
    else:
        confusionMatrix[row[0]][predicted_label] += 1

print(confusionMatrix)

for name in confusionMatrix.keys():
    ansSum = 0
    for vals in confusionMatrix[name].values():
        ansSum += vals
    print(f"{name}, ACCURACY: {confusionMatrix[name][name] / ansSum * 100}%")