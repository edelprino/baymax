from __future__ import print_function
import pandas as pd
import numpy as np
from sklearn import tree

filename = "var/titanic_dataset.csv"
dataset = pd.read_csv(filename)
dataset = dataset.replace({"sex": {"male": 0, "female": 1}})
# Add family_size value
dataset["family_size"] = dataset["sibsp"] + dataset["parch"] + 1

target = dataset["survived"].values
features = dataset[["pclass", "sex", "age", "fare", "sibsp", "parch", "family_size"]].values

# Fit your first decision tree: decisional_tree
decisional_tree = tree.DecisionTreeClassifier(max_depth = 10, min_samples_split = 5, random_state = 1)
decisional_tree = decisional_tree.fit(features, target)

# Look at the importance of the included features
# print(decisional_tree.feature_importances_)

# Let"s create some data for DiCaprio and Winslet
dicaprio = [3, 0, 19, 5.0000, 0, 0, 0]
winslet = [1, 1, 17, 100.0000, 0, 0, 0]
# Predict surviving chances (class 1 results)
prediction = decisional_tree.predict([dicaprio, winslet])
print("Score: ", decisional_tree.score(features, target))
print("DiCaprio survived:", prediction[0])
print("Winslet survived:", prediction[1])