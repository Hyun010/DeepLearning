import tensorflow as tf
import json
from model import get_model
from dataloader import get_dataloader

classes = ['apple', 'mandarine']
qualities = ['good', 'bad']
train_folder_name = 'Training'

model = get_model(classes, qualities)
dataloader = get_dataloader(classes, qualities, train_folder_name)

model.compile(loss=tf.keras.losses.categorical_crossentropy, metrics=tf.keras.metrics.categorical_accuracy)
model.fit(dataloader, callbacks=[tf.keras.callbacks.ModelCheckpoint('./models/train_model.h5')], epochs=5)




