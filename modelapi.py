# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:24:36 2020

@author: s1430
"""

from keras.models import Model
from keras.layers import Input, Dense

a = Input(shape=(32, ))
b = Dense(32)(a)
model = Model(inputs = a, outputs = b)

model = Model(inputs = [a1, a2], outputs = [b1, b2, b3])

compile(optimizer, loss=None, metrics=None, loss_weights = None, sample_weight_mode = None,weighted_metrics=None, target_tensors=None)
