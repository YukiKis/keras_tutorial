# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:30:25 2020

@author: s1430
"""


from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.layers import Input, LSTM, Embedding, Dense
from keras.models import Sequential, Model

vision_model = Sequential()
vision_model.add(Conv2D(64, (3, 3), activation="relu", padding="same", input_shape=(224, 224, 3)))
vision_model.add(Conv2D(64, (3, 3), activation="relu"))
vision_model.add(MaxPooling((2, 2)))
vision_model.add(Conv2D(128, (3, 3), activation="relu", padding="same"))
vision_model.add(Conv2D(128, (3, 3), activation="relu"))
vision_model.add(MaxPooling2D((2, 2)))
vision_model.add(Conv2D(256, (3, 3), activation="relu", padding="same"))
vision_model.add(Conv2D(256, (3, 3), activation="relu"))
vision_model.add(Conv2D(256, (3, 3), activation="relu"))
vision_model.add(MaxPooling((2, 2)))
vision_model.add(Flatten())

image_input = Input(shape=(224, 224, 3))
encoded_image = vision_model(image_input)

question_input = Input(shape=(100, ), dtype="int32")
embedded_question = Embedding(input_dim = 10000, output_dim = 256, input_length = 100)(question_input)
encoded_question = LSTM(256)(embedded_question)

merged = keras.layers.concatnated([encoded_question, encoded_image])
output = Dense(1000, activation="softmax")(merged)
vqa_model = Model(inputs = [image_input, question_input], outputs=output)
