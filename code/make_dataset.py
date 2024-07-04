# AI Hub에서 제공 받은 데이터를 학습 할 수 있게 데이터의 저장 방식을 바꿔 주는 기능을 해주는 코드

import os  # 폴더를 만들고, 폴더안에 파일들을 검색해주는 라이브러리
import zipfile  # 압축을 해제하는데 이용하는 라이브러리

classes = ["apple", "mandarine"]  # 학습은 사과와 귤을 분류하는 모델이기 때문에 데이터 역시 사과와 귤만 학습 데이터로 저장
# 참고
# 만약 사과와 귤 그리고 마늘 3개의 클래스를 분류하는 모델을 만들고 싶은 경우
# classes = ["apple", "mandarine", "galic"] 으로 고치고,
# 18, 26, 32, 40,41, 56~60 번째 줄의 주석을 의미하는 #을 제거하고,
# 윗 줄과 들여쓰기를 맞춰주고 make_dataset.py를 실행시키면, 3개의 클래스를 학습시킬 수 있게 데이터를 저장해 준다.

download_folder_name = "농산물 품질(QC) 이미지" # AI Hub에서 다운 받은 폴더 이름
train_folder_name = "train"  # 저장될 폴더 이름
specific_image_name = "FR45"  # 1개 과일에 대해서 5개의 각도에서 촬영된 이미지가 있으나 1개의 각도 이미지만 학습에 이용



LABEL_FILE_NAME = '[라벨]'
CLASS_0_NAME = classes[0]  # 'apple'
CLASS_1_NAME = classes[1]  # 'mandarine'
# CLASS_2_NAME = classes[2]  # 'galic'


os.makedirs(train_folder_name, exist_ok=True)  # train_folder_name에 저장된 train이라는 이름의 폴더를 만들어 준다.

idx = 0
os.makedirs(f'{train_folder_name}/{CLASS_0_NAME}', exist_ok=True)
os.makedirs(f'{train_folder_name}/{CLASS_1_NAME}', exist_ok=True)
# os.makedirs(f'{train_folder_name}/{CLASS_2_NAME}', exist_ok=True)
# 각 클래스별로 train폴더 안에 이름을 가지는 폴더를 따로 만들어 준다.

zip_file_list = os.listdir(f'{download_folder_name}/Training')
# AI Hub에서 내려 받은 데이터 중, Training에 있는 압축파일만 활용하기 위해 Training추가

class0_file_list = []
class1_file_list = []
# class2_file_list = []
print(zip_file_list)
for zip_file_name in zip_file_list:
    if not (LABEL_FILE_NAME in zip_file_name): # [라벨] 이 포함되지 않은 압축파일만 활용
        if CLASS_0_NAME in zip_file_name: # apple이 포함된 파일을 따로 추려 내는 코드
            class0_file_list.append(zip_file_name)
        elif CLASS_1_NAME in zip_file_name: # mandarine이 포함된 파일을 따로 추려 내는 코드
            class1_file_list.append(zip_file_name)
        # elif CLASS_2_NAME in zip_file_name: # galic이 포함된 파일을 따로 추려 내는 코드
        #     class2_file_list.append(zip_file_name)

for class0_file in class0_file_list:
    zip_file = zipfile.ZipFile(f'{download_folder_name}/Training/{class0_file}')  # 압축파일을 파이썬에서 여는 코드
    for file in zip_file.filelist:  # 열린 압축 된 각각의 파일들을 하나씩 검색하는 코드
        if specific_image_name in file.filename:  # 압축된 파일 모두를 사용하지 않기 때문에, FR45라는 파일 이름이 있는 이미지만 선택하는 코드
            zip_file.extract(file.filename, f'{train_folder_name}/{CLASS_0_NAME}')  # 해당 이미지를 압축파일에서 압축을 풀어 train/class폴더로 옮기는 코드


for class1_file in class1_file_list:
    zip_file = zipfile.ZipFile(f'{download_folder_name}/Training/{class1_file}')
    for file in zip_file.filelist:
        if specific_image_name in file.filename:
            zip_file.extract(file.filename, f'{train_folder_name}/{CLASS_1_NAME}')

# for class2_file in class2_file_list:
#     zip_file = zipfile.ZipFile(f'{download_folder_name}/Training/{class2_file}')
#     for file in zip_file.filelist:
#         if specific_image_name in file.filename:
#             zip_file.extract(file.filename, f'{train_folder_name}/{CLASS_2_NAME}')

