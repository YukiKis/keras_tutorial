# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:47:08 2020

@author: s1430
"""

compile(self, optimizer, loss, metrics=None, sample_weight_mode=None, weighted_metrics=None, target_tensors=None)

model = Sequential()
model.add(Dense(32, input_shape=(500, )))
mode.add(Dense(10, activation="softmax"))
model.copmile(optimizre="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])

fit(self, x=None, y=None, batch_size=None, epochs=1, verbose=1, callbacks=None, validation_split=0, validation_data=None, shuffle=True, class_weight=None, sample_weight=None, initial_epoch=0, steps_per_epoch=None, validation_steps=None)

evaluate(self, x=None, y=None, batch_size=None, verbose=1, sample_weight=None, steps=None)

predict(self, x, batch_size=None, verbose=0, steps=None)

train_on_batch(self, x, y, class_weight=None, sample_weight=None)

test_on_batch(self, x, y, sample_weight=None)

predict_on_batch(self, x)

fit_generator(self, generator, steps_per_epochs=None, epochs=1, verbose=1, callbacks=None, validation_data=None, validation_steps=None, class_weight=none, max_queue_size=10, workers=1, use_multiprocessin=False, shuffle=True, initial_epochs=0)

def generate_arrays_from_file(path):
    while 1:
        with open(path) as f:
            for line in f:
                x, y  = process_line(line)
                yield(x, y)
mode.fit_generator(generate_arrays_from_file("/my_file.txt"), steps_per_epoch = 1000, epochs=10)

evaluate_generator(self, generator, steps=None, max_queue_size=10, workers=1, use_multiprocessing=False)

predict_generator(self, generator, steps=None, max_queue_size=10, workers=1, use_multiprocessing=False, verbose=0)

get>_layer(self, name=None, index=None)