# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:33:34 2020

@author: s1430
"""


keras.layers.Dense(units, activation=None, use_bias=True, kernel_initializer="glorot_uniform", bias_initializer="zeros", kernel_regularizer=None, bias_regularizer=None, kernel_cunstraint=None, bias_constraint=None)

model = Sequeneial()
model.add(Dense(32, input_shape=(16, )))
model.add(Dense(32))

keras.layers.Activation(activation)

keras.layers.Dropout(rate, noise_shape=None, seed=None)

keras.layers.Flatten()

model = Sequential()
model.add(Conv2D(64, (3, 3), border_mode="same", input_shape=(3, 32, 32)))
model.add(Flatten())

keras.engine.topology.Input()

x = Input(shape=(32, ))
y = Dense(16, activation="softmax")(x)
model = Model(x, y)

keras.layers.reshape(target_shape)

model = Sequential()
model.add(Reshape(3, 4), input_shape=(12, ))
model.add(Reshape(6, 2))
model.ad(Reshape(-1, 2, 2))

keras.layers.Permute(dims)

model = Sequential()
model.add(Permute((2, 1), input_shape=(10, 64)))

keras.layers.RepeatVector(n)

model = Sequential()
model.add(Denes(32, input_dim=32))
model.add(RepeatVector(3))

keras.layers.Lambda(function, output_shape=None, mask=None, arguments=None)
model.add(Lambda(lambda x: x ** 2))


keras.layers.ActivityRegularization(l1 = 0.0, l2=0.0)

keras.layers.Masking(mask_value=0.0)
model = Sequential()
model.add(Masking(mask_value=0, input_shape=(timesteps, features))
model.add(LSTM(32)))