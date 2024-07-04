import os
from model import get_model
import glob
from dataloader import load_image
import numpy as np

MODEL_FILE_NAME = './models/train_model.h5'  # 학습한 딥러닝 모델의 결과값이 저장된 파일

classes = ['apple', 'mandarine']  # 분류 클래스 종류
qualities = ['good', 'bad']  # 분류 품질 종류
train_folder_name = 'Validation'  # 검정 데이터가 저장된 폴더 이름

model = get_model(classes, qualities)  # 딥러닝 모델을 초기화 하는 코드

model.load_weights(MODEL_FILE_NAME)  # 학습한 딥러닝 모델을 불러오는 코드

file_list = glob.glob(os.path.join(train_folder_name, '**', '*.png'), recursive=True)
# train_folder_name폴더 안에 있는 이미지 이름을 모두 불러오는 코드

total = 0  # 총 데이터의 갯수가 들어갈 변수
class_correct = 0  # 그 중 분류가 맞은 데이터의 갯수가 들어갈 변수
quality_correct = 0  # 그 중 품질 예측이 맞은 데이터의 갯수가 들어갈 변수

for file_name in file_list:
    img = load_image(file_name)  # train폴더 안에 있는 이미지 파일 1개를 파이썬으로 읽는코드
    prediction = model.predict(img[None])  # 읽은 이미지를 딥러닝 모델을 통해서 분류와 품질 예측
    # 딥러닝 분류 결과를 실제 분류 항목 이름으로 변경해주는 코드
    class_prediction = prediction[0]  # 딥러닝 모델의 결과 중 분류 결과만 가져와 class_prediction에 저장
    class_result = np.argmax(class_prediction[0])
    class_predict_label = classes[class_result]
    # 그 두개의 값 중, 0번째에 있는 값이 크다면 사과로 1번째에 있는 값이 크면 귤로 설정 해주는 코드
    # 딥러닝 품질 예측 결과를 실제 품질 항목 이름으로 변경해주는 코드
    quality_prediction = prediction[1]  # 딥러닝 모델의 결과 중 품질 예측 결과만 가져와 quality_prediction에 저장
    quality_result = np.argmax(quality_prediction[0])
    quality_predict_label = qualities[quality_result]
    # 그 두개의 값 중, 0번째에 있는 값이 크다면 good으로 1번째에 있는 값이 크면 bad로 설정 해주는 코드

    if class_predict_label in file_name:
        # 분류가 맞는 경우 +1
        class_correct = class_correct + 1
    if quality_predict_label in file_name:
        # 품질이 맞는 경우 +1
        quality_correct = quality_correct + 1
    total = total + 1  # 전체 테스트 이미지 갯수

class_accuracy = round(class_correct / total * 100, 2)
quality_accuracy = round(quality_correct / total * 100, 2)
print(f"평가 데이터에 대해서 과일의 분류 정확도는 {class_accuracy}% 입니다.")
print(f"평가 데이터에 대해서 과일의 품질 예측 정확도는 {quality_accuracy}% 입니다.")
