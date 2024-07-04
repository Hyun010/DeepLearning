import os
import glob
import random
import tensorflow as tf
from PIL import Image
import numpy as np


def load_image(file_name):
    img = Image.open(file_name)
    img = img.resize((128, 128))
    img = np.asarray(img).astype(np.float32)
    return img / 255


def get_dataloader(classes, qualities, img_folder_name):
    file_list = glob.glob(os.path.join(img_folder_name, '**', '*.png'), recursive=True)
    random.shuffle(file_list)
    return DataGenerator(file_list, classes, qualities)


class DataGenerator(tf.keras.utils.Sequence):
    def __init__(self, a_file_list, a_classes, a_qualities, a_batch_size=32):
        self.file_list = a_file_list
        self.classes = a_classes
        self.qualities = a_qualities
        self.batch_size = a_batch_size

    def __len__(self):
        return len(self.file_list) // self.batch_size

    def __getitem__(self, a_idx):
        batch_image = []
        batch_class_label = []
        batch_quality_label = []
        for file_name in self.file_list[a_idx * self.batch_size : (a_idx + 1) * self.batch_size]:
            img = load_image(file_name)
            class_label = [(class_name in file_name) for class_name in self.classes]
            quality_label = [(quality_name in file_name) for quality_name in self.qualities]
            batch_image.append(img)
            batch_class_label.append(class_label)
            batch_quality_label.append(quality_label)
        return np.asarray(batch_image, dtype=np.float32), {'class': np.asarray(batch_class_label, dtype=np.float32), 'quality': np.asarray(batch_quality_label, dtype=np.float32)}



