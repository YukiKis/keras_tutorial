# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:31:27 2020

@author: s1430
"""


from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D

model = Sequential()
model.add(Conv1D(64, 3, acitvation="relu", input_shape=(seq_length, 100)))
model.add(Conv1D(64, 3, activation="relu"))
model.add(MaxPooling1D(3))
model.add(Conv1D(128, 3, activation="relu"))
model.add(Conv1D(128, 3, activation="relu"))
model.add(GlobalAveragePooling1D())
model.add(Dropout(0.5))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy",
              optimizer="rmsprop",
              metrics=["accuracy"]
              )
model.fit(x_train, y_train, epochs=10, batch_size=16)
score = model.evaluate(x_test, y_test, batch_size=16)

