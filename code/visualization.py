import glob, os
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

from model import get_model
from dataloader import load_image
from utils import make_gradcam_heatmap
from PIL import Image

classes = ['apple', 'mandarine']
MODEL_FILE_NAME = './models/train_model.weights.h5'

result_folder_name = 'result'
correct_folder_name = 'POSITIVE' # result 폴더에 맞춘 이미지가 들어 있는 폴더 이름
incorrect_folder_name = 'NEGATIVE' # result 폴더에 틀린 이미지가 들어 있는 폴더 이름

gradcam_folder_name = 'gradcam' # grad cam result가 저장될 폴더 이름
os.makedirs(gradcam_folder_name)
os.makedirs(f'{gradcam_folder_name}/{correct_folder_name}') # 각각 들린 이미지에 대한 결과는 NEGATIVE폴더안에
os.makedirs(f'{gradcam_folder_name}/{incorrect_folder_name}') # 맞춘 이미지에 대한 결과는 POSITIVE폴더 안에 저장됩니다.

model = get_model(classes)
model.load_weights(MODEL_FILE_NAME)

incorrect_file_list = glob.glob(os.path.join(result_folder_name, '*', incorrect_folder_name, '*.*'), recursive=True)
# result folder에 각각 사과와 귤 폴더안에 NEGATIVE라는 폴더안에 있는 이미지 파일목록을 불러오는 코드
correct_file_list = glob.glob(os.path.join(result_folder_name, '*', correct_folder_name, '*.*'), recursive=True)
# result folder에 각각 사과와 귤 폴더안에 POISTIVE라는 폴더안에 있는 이미지 파일목록을 불러오는 코드

idx = 0
for file_name in correct_file_list: # 정답을 맞춘 이미지에 대해서 한장씩 gradcam 결과를 시각화
    img = load_image(file_name)
    f, ax = plt.subplots(1, 3)
    plt.suptitle("Grad Cam Result")
    grads = make_gradcam_heatmap(img[None], model)
    jet_heatmap = np.uint8(cm.rainbow(grads)[..., :3] * 255)
    jet_heatmap = Image.fromarray(jet_heatmap)
    img = Image.open(file_name)
    img = np.asarray(img.resize((64, 64)).convert('RGB'))
    jet_heatmap = np.asarray(jet_heatmap.resize((64, 64)))
    ax[0].imshow(img)
    ax[1].imshow(jet_heatmap)
    ax[2].imshow(np.uint8(np.clip(img * 0.5 + jet_heatmap * 0.5, 0, 255)))
    plt.savefig(f'{gradcam_folder_name}/{correct_folder_name}/{os.path.split(file_name)[-1]}')
    f.clf()
    plt.clf()
    plt.close()

idx = 0
for file_name in incorrect_file_list: # 정답을 맞추지 못한 이미지에 대해서 한장씩 gradcam 결과를 시각화
    img = load_image(file_name)
    f, ax = plt.subplots(1, 3)
    plt.suptitle("Grad Cam Result")
    grads = make_gradcam_heatmap(img[None], model)
    jet_heatmap = np.uint8(cm.rainbow(grads)[..., :3] * 255)
    jet_heatmap = Image.fromarray(jet_heatmap)
    img = Image.open(file_name)
    img = np.asarray(img.resize((64, 64)).convert('RGB'))
    jet_heatmap = np.asarray(jet_heatmap.resize((64, 64)))
    ax[0].imshow(img)
    ax[1].imshow(jet_heatmap)
    ax[2].imshow(np.uint8(np.clip(img * 0.5 + jet_heatmap * 0.5, 0, 255)))
    plt.savefig(f'{gradcam_folder_name}/{incorrect_folder_name}/{idx}.png')
    f.clf()
    plt.clf()
    plt.close()
    idx += 1






