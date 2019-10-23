from __future__ import print_function

import numpy as np
import tflearn
from tflearn.datasets import titanic
from tflearn.data_utils import load_csv

# Download the Titanic dataset
titanic.download_dataset('titanic_dataset.csv')

import pandas as pd
dataset = pd.read_csv('titanic_dataset.csv')
dataset = dataset.drop(columns='name').drop(columns='ticket')
dataset['sex'] = dataset['sex'].apply(lambda sex: 1 if sex == 'female' else 0)
labels = pd.get_dummies(dataset.pop('survived')).values
data = dataset.values

# Build neural network
net = tflearn.input_data(shape=[None, 6])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 2, activation='softmax')
net = tflearn.regression(net)

# Define model
model = tflearn.DNN(net)
# Start training (apply gradient descent algorithm)
model.fit(data, labels, n_epoch=20, batch_size=16, show_metric=True)

# Let's create some data for DiCaprio and Winslet
dicaprio = [3, 0, 19, 0, 0, 5.0000]
winslet = [1, 1, 17, 1, 2, 100.0000]
# Preprocess data
# dicaprio, winslet = preprocess([dicaprio, winslet], to_ignore)
# Predict surviving chances (class 1 results)
pred = model.predict([dicaprio, winslet])
print("DiCaprio Surviving Rate:", pred[0][1])
print("Winslet Surviving Rate:", pred[1][1])
