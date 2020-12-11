# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:23:34 2020

@author: s1430
"""


from keras.layers import Conv2D, Input

x = Input(shape=(256, 256, 3))
y = Conv2D(3, (3, 3), padding="same")(x)
z = keras.layers.add([x, y])

