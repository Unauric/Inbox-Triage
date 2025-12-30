import sys
import nb_model
from nb_model import NaiveBayesModel

modelPath = sys.argv[1]
text = sys.argv[2]

model = nb_model.NaiveBayesModel.from_dict(modelPath)
print(model.Predict(text))
