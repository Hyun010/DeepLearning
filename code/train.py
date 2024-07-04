import tensorflow as tf
import json
from model import get_model
from dataloader import get_dataloader

classes = ['apple', 'mandarine']
train_folder_name = 'train'

model = get_model(classes)
dataloader = get_dataloader(classes, train_folder_name)
model.compile(loss=tf.keras.losses.categorical_crossentropy, metrics=[tf.keras.metrics.categorical_accuracy])
model.fit(dataloader, callbacks=[tf.keras.callbacks.ModelCheckpoint(filepath='./models/train_model.weights.h5',save_weights_only=True)])

