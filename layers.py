# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:29:28 2020

@author: s1430
"""


layer = Dense(32)
config = layer.get_config()
reconstructed_layer = Dense.from_config(config)

from keras import layers

config = layer.get_config()
layer = layers.deserialize({"class_name": layer.__class__.__name__, "config": config})

layer.input
layer.output
layer.input_shape
layer.output_shape

layer.get_input_at(node_index)
layer.get_output_at(node_index)
layer.get_input_shape_at(node_index)
layer.get_output_shape_at(node_index)

