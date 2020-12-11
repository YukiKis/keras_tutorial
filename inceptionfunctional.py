# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:17:36 2020

@author: s1430
"""


from keras.layers import Conv2D, MaxPooling2D, Input

input_img = Input(shape=(256, 256, 3))

tower_1 = Conv2D(64, (1, 1), padding="same", activation="relu")(input_img)
tower_1 = Conv2D(64. (3, 3), padding="same", activation="relu")(tower_1)

towre_2 = Conv2D(64, (1, 1), padding="same", activation="relu")(input_img)
tower_2 = Conv2D(64, (5, 5), padding="same", activation="relu")(tower_2)

towre_3 = MaxPooling2D((3, 3), strides=(1, 1), padding="same")(input_img)
tower_3 = Conv2D(64, (1, 1), padding="same", activation="relu")(tower_3)

output = keras.layers.concatnate([tower_1, tower_2, tower_3], axis=1)