# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:41:07 2020

@author: s1430
"""

import keras
from keras.layers import TimeDistribution
from keras.layers import LSTM, Dense

video_input = Input(shape=(100, 224, 224, 3))
encoded_frame_sequence = TimeDistributed(vision_model)(video_input)
encoded_video = LSTM(245)(encoded_frame_sequence)

question_encoder = Model(inputs = question_input, outputs = encoded_question)

video_question_input = Input(shape=(100, ), dtype="int32")
encoded_video_question = question_encoder(video_question_input)

merged = keras.layers.concatnate([encoded_video, encoded_video_question])
output = Dense(1000, activation="softmax")(merged)
video_qa_model = Model(inputs=[video_input, video_question_model], outputs = output)

