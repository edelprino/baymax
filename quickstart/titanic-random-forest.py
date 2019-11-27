from __future__ import print_function
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

filename = "var/titanic_dataset.csv"
dataset = pd.read_csv(filename)
dataset = dataset.replace({"sex": {"male": 0, "female": 1}})

features = dataset[["pclass", "sex", "age", "fare", "sibsp", "parch"]].values
target = dataset["survived"].values

# Building and fitting the_forest
forest = RandomForestClassifier(max_depth = 10, min_samples_split=2, n_estimators = 100, random_state = 1)
the_forest = forest.fit(features, target)

# Look at the importance of the included features
# print(the_forest.feature_importances_)

dicaprio = [3, 0, 19, 5.0000, 0, 0]
winslet = [1, 1, 17, 100.0000, 0, 0]
prediction = the_forest.predict([dicaprio, winslet])
print("Score: ", the_forest.score(features, target))
print("DiCaprio survived:", prediction[0])
print("Winslet survived:", prediction[1])