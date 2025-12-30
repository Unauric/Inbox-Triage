import json
import math


class NaiveBayesModel:

    # Example Class constructor

    def __init__(self):
        self.classMessageCounter = {}
        self.classWordCounter = {}
        self.classWordFrequency = {}
        self.vocabularyLength = 0


    # Method belongs to the class itself only not to any object
    # We would call it like this: model = NaiveBayesModel.from_dict()
    # This method creates a new object of this class
    # Works as an alternative constructor
    @classmethod
    def from_dict(cls, model_dict):
        # cls - class object, same way as 'self'
        with open(model_dict, "r") as f:
            data = json.load(f)

        # calling cls() creates a new instance of class object
        model =cls()
        model.classMessageCounter = data['messagesPerClass']
        model.classWordCounter = data['sumOfWordsInClass']
        model.classWordFrequency = data['wordFrequencyDic']
        model.vocabularyLength = data['vocabulary length']
        return model



    def log_prob_word(self, word, msgClass):
        N_C_w = self.classWordFrequency[msgClass].get(word, 0)
        N_C_t = self.classWordCounter[msgClass]
        P_w_c = (N_C_w + 1) / (N_C_t + self.vocabularyLength)
        return math.log(P_w_c)


    def score(self, tokens):
        val = {}
        sumofMessages = self.MessageSum()
        for msgClass in self.classMessageCounter:
            P_C = math.log(self.classMessageCounter[msgClass] / sumofMessages)
            val[msgClass] = P_C
            for token in tokens:
                if msgClass not in val:
                    val[msgClass] = 0
                val[msgClass] += self.log_prob_word(token, msgClass)

        return val

    def MessageSum(self):
        sum = 0
        for msgClass in self.classMessageCounter:
            sum += self.classMessageCounter[msgClass]
        return sum

    # This function returns two things:
    # a label and a scores_dict.
    def Predict(self, text) -> tuple[str, dict]:
        words = text.split(' ')
        scores = self.score(words)
        label = max(scores, key=scores.get)
        return label, scores






#a = NaiveBayesModel.from_dict()
#print(a.Predict("WIN a free iPhone now!!!"))