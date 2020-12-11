# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:28:52 2020

@author: s1430
"""


from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM

model = Sequential()
model.add(Embedding(max_features, output_dim=256))
model.add(LSTM(128))
model.add(Dropout(0.5))
model.add(Dense(1, activation="sigmoid"))

model.compile8(loss="binary_crossentropy",
               optimizer="rmsprop",
               metrics=["accuracy"]
               )
model.fit(x_train, y_train, batch_size=16, epochs=10)
score = model.evaluate(x_test, y_test, batch_size=16)
