# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(units = 64, activation = "relu", input_dim = 100))
model.add(Dense(units = 10, activation = "softmax"))

model.compile(loss = "categorical_crossentropy",
              optimizer = "sgd",
              metrics = ["accuracy"])

# model.compile{loss = keras.losses.categoricao_entropy,
#                optimizer = keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov = True)})

model.fit(x_train, y_train, epochs=5, batch_size=32)
model.train_on_batch(x_batch, y_batch)

loss, metrics = model.evaluate(x_test, y_test, batch_size=100)
classes = model.predict(x_test, batch_size=128)