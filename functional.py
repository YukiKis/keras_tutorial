# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:32:21 2020

@author: s1430
"""


from keras.layers import Input, Dense
from keras.models import Model

inputs = Input(shape=(784, ))
x = Dense(64, activation="relu")(inputs)
x = Dense(64, activation="relu")(x)
predictions = Dense(10, activation="softmax")(x)

model = Model(inputs = Inputs, outputs = predictions)
model.compile(optimizer="rmsprop",
              loss="categorical_crossentropy",
              metrics=["accuracy"]
              )
model.fit(data, labels)

###

x = Input(shape=(784, ))
y = model(x)

###

from keras.layers import TimeDistribution
input_sequences = Input(shape=(20, 784))
processed_sequences = TimeDistribution(model)(input_sequences)

###

from keras.layers import Input, Embedding, LSTM, Dense
from keras.models import Model

main_input = Input(shape=(100, ), dtype="int32", name="main_input")
x = Embedding(output_dim=512, input_dim = 10000, input_length=100)(main_input)
lstm_out = LSTM(32)(x)
auxiality_output = Dense(1, activation="sigmoid", name="aux_output")(lstm_out)
auxiality_input = Input(shape=(5, ), name="aux_input")
x = keras.layers.concatnate([lstm_out, auxiality_input])
x = Dense(64, activation="relu")(x)
x = Dense(64, activation="relu")(x)
x = Dense(64, activation="relu")(x)
main_output = Dense(1, activation="sigmoid", name="main_output")(x)

model = Model(inputs = [main_input, auxiality_input], outputs = [main_output, auxiality_output])
model.compile(optimizer="rmsprop", loss="binary_crossentropy", loss_weights=[1., 0.2])
model.fit([heading_data, additional_data], [labels, labels], epochs=50, batch_size=32)

model.compile(optimizer="rmsprop", loss={"main_output": "binary_crossentropy", "aut_output": "binary_crossentropy"},
              loss_weights={"main_output": 1, "aux_output": 0.2})
model.fit({"main_input": heading_data, "aux_input": additional_data}, {"main_output": labels, "aut_output": labels}, epochs=50, batch_size-32)

###

import keras
from keras.layers import Input, LSTM, Dense
from keras.models import Model

tweet_a = Input(shape=(280, 256))
tweet_b = Input(shape=(280, 256))

shared_lstm = LSTM(64)
encoded_a = shared_lstm(tweet_a)
encoded_b = shared_lstm(tweet_b)
merged_vector = keras.layers.concatnate([encoded_a, encoded_b], axis=-1)
predictions = Dense(1, activation="sigmoid")(merged_vector)

model = Model(inputs = [tweet_a, tweet_b], outputs = predictions)
model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])
odel.fit([data_a, data_b], labels, epochs=10)

a = Input(shape=(280, 256))
lstm = LSTM(32)
encoded_a = lstm(a)
lstm.output == encoded_a

a = Input(shape=(280, 256))
b = Input(shape=(280, 256))
lstm = LSTLM(32)
encoded_a = lstm(a)
encoded_b = lstm(b)

lstm.get_output_at(0)
lstm.get_output_at(1)

a = Input(shape=(32, 32, 3))
b = Input(shape=(64, 64, 3))

conv = Conv2D(16, (3, 3), padding="same")
conved_a = conv(a)
conved_b = conb(b)

conv.input_shape
conv.get_input_shape_at(0)
cont.get_input_shape_at(1)