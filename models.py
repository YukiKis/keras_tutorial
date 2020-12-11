# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:34:20 2020

@author: s1430
"""

config = model.get_config()
model = Model.from_config(conig)
model = Sequential.from_comfig(config)
model.get_weights()
model.set_weights(weights)
model.to_json()
from keras.models import model_from_json

json_string = model.to_json()
model = model_from_json(json_string)

from keras.models import model_from_yaml
yaml_string = model.to_yaml()
model = model_from_yaml(yaml_string)

model.save_weights(filepath)
model.load_weights(filepath, by_name=False)

import keras

class SimpleMLP(keras.model):
    def __init__(self, use_bn=Fale, use_dp=False, num_classes=10):
        super(SImpleMLP, self).__init__(name="mlp")
        serf.use_bn = use.bn
        self.use_dp = use_dp
        self.num_classes = num_classes
        
        self.dense1 = keras.layers.Dense(32, activation="relu")
        self.dense2 = keras.laysers.Dense(num_classes, activation="softmax")
        
        if self.use_dp:
            self.dp = keras.layers.Dropout(0.5)
        if self.use_bn:
            self.bn(x) = keras.layers.BatchNormalization(axis=-1)
    
    def call(self, inputs):
        x = self.dense1(inputs)
        if self.use_dp:
            x = self.dp(x)
        if self.use_bn:
            x = self.bn(x)
        return self.dense2
    
model = SimpleMLP()
model.compile(...)
model.fit(...)