# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:25:02 2020

@author: s1430
"""


from keras.layers import Conv2D, MaxPooling2D, Input, Dense, Flatten
from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D, Input, Dense, Flatten
from keras.models import Model

digit_input = Input(shape=(27, 27, 1))
x = Conv2D(64, (3, 3))(digit_input)
x = Conv2D(64, (3, 3))(x)
x = MaxPooling2D((2, 2))(x)
out = Flatten()(x)

vision_model = Model(digit_input, out)

digit_a = Input(shape=(27, 27, 1))
digit_b = Input(shape=(27, 27, 1))

out_a = vision_model(digit_a)
out_b = vision_model(digit_b)

concatnated = keras.layers.concatnate([out_a, out_b])
out = Dense(1, activation="sigmoid")(concatnated)

classification_model = Model([digit_a, digit_g], out)
