# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 09:31:31 2020

@author: s1430
"""

import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import keras.backend as K

mdoel = Sequential([
        Dense(32, input_shape = (784, )),
        Activation("relu"),
        Dense(10),
        Activation("softmax"),
        ]
)

model = Sequential()
model.add(Dense(32, input_dim = 784))
model.add(Activation("relu"))

model = Sequential()
model.add(Dense(32, input_shape = (784, )))

model = Sequential()
model.add(Dense(32, input_dim = 784))

model.compile(optimizer = "rmsprop",
              loss = "categorical_crossentropy",
              metrics = ["accuracy"]
              )
model.compile(optimizer = "rmsprop",
              loss = "binary_crossentropy",
              metrics = ["accuracy"]
              )
model.compile(optimizer = "rmsprop",
              loss = "mse"
              )

def mean_pred(y_true, y_pred):
    return K.mean(y_pred)

model.compile(optimizer = "rmsprop",
              loss = "binary_crossentropy",
              metrics = ["accuracy", mean_pred]
              )

model = Sequential()
model.add(Dense(32, activation = "relu", input_dim = 100))
model.add(Dense(1, activation = "sigmoid"))
model.compile(optimizer = "rmsprop",
              loss = "binary_crossentropy",
              metrics = ["accuracy"]
              )

data = np.random.random((1000, 100))
labels = np.random.randint(2, size = (1000, ))
model.fit(data, labels, epochs = 10, batch_size = 32)
loss, accuracy = model.evaluate(data, labels)

model = Sequential()
model.add(Dense(32, activation = "relu", input_dim = 100))
model.add(Dense(10, activation = "softmax"))
model.compile(optimizer = "rmsprop",
              loss = "categorical_crossentropy",
              metrics = ["accuracy"]
              )

data = np.random.random((1000, 100))
labels - np.random.randint(10, size=(1000, 1))
one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)
model.fit(data, one_hot_labels, epochs=10, batch_size=32)
loss, accuracy = model.evaluate(data, one_hot_labels)

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import numpy as np

x_train = np.random.random((1000, 20))
y_train = keras.utils.to_categorical(np.random.randint(10, size=(1000, 1)), num_classes=10)
x_test = np.random.random((100, 20))
y_test = keras.utils.to_categorical(np.random.randint(10, size=(100, 1)), num_classes=10)

model = Sequential()
model.add(Dense(64, activation="relu", input_dim=20))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(10, activation="softmax"))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss="categorical_crossentropy",
              optimizer=sgd,
              metrics = ["accuracy"]
              )
model.fit(x_train, y_train, epochs=20, batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)
