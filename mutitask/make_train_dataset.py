# AI Hub에서 제공 받은 데이터를 학습 할 수 있게 데이터의 저장 방식을 바꿔 주는 기능을 해주는 코드

import os, glob, json
import zipfile



classes = ["apple", "mandarine"]  # 분류할 클래스 종류
CLASS_0_NAME = classes[0]  # 'apple' 첫번째 클래스
CLASS_1_NAME = classes[1]  # 'mandarine' 두번째 클래스

DOWNLOAD_FOLDER_NAME = '농산물 품질(QC) 이미지'  # '농산물 품질(QC) 이미지'

SAVE_DIRECTORY_NAME = 'Training'  # 농산물 품질(QC) 이미지에서 학습 이미지(Training)가 들어있는 폴더 이름

specific_image_name_1 = "FR45"  # 학습에 이용할 각도의 이름

qualities = ["good", "bad"]
good_img_folder = qualities[0]  # 품질이 상인 이미지들이 들어갈 폴더 이름
bad_img_folder = qualities[1]  # 품질이 하인 이미지들이 들어갈 폴더 이름

os.makedirs(SAVE_DIRECTORY_NAME, exist_ok=True)  # 학습에 이용할 이미지가 들어갈 폴더 생성

os.makedirs(f'{SAVE_DIRECTORY_NAME}/{CLASS_0_NAME}', exist_ok=True)  # 첫번째 종류(사과) 폴더 생성
os.makedirs(f'{SAVE_DIRECTORY_NAME}/{CLASS_1_NAME}', exist_ok=True)  # 첫번째 종류(귤) 폴더 생성

zip_file_list = os.listdir(f'{DOWNLOAD_FOLDER_NAME}/{SAVE_DIRECTORY_NAME}')  # 학습 이미지가 들어있는 폴더에 이미지가 압축된 압축 파일 리스트를 조회

class0_file_list = [] # 첫번째 클래스 이미지 들이 들어있는 압축파일이 이름이 저장될 리스트
class1_file_list = [] # 두번째 클래스 이미지 들이 들어있는 압축파일이 이름이 저장될 리스트

for zip_file_name in zip_file_list:
    if CLASS_0_NAME in zip_file_name:  # 첫번째 클래스 이미지의 압축파일 이름은 class0_file_list에 저장
        class0_file_list.append(zip_file_name)
    elif CLASS_1_NAME in zip_file_name:  # 두번째 클래스 이미지의 압축파일 이름은 class0_file_list에 저장
        class1_file_list.append(zip_file_name)

for class0_file in class0_file_list:  # 첫번째 클래스의 압축파일을 하나씩 읽어서 이미지(png)와 설명(json)파일을 Training폴더의 class1(사과) 폴더에 저장
    zip_file = zipfile.ZipFile(f'{DOWNLOAD_FOLDER_NAME}/{SAVE_DIRECTORY_NAME}/{class0_file}')
    for file in zip_file.filelist:
        if specific_image_name_1 in file.filename:
            zip_file.extract(file.filename, f'{SAVE_DIRECTORY_NAME}/{CLASS_0_NAME}')


for class1_file in class1_file_list:  # 두번째 클래스의 압축파일을 하나씩 읽어서 이미지(png)와 설명(json)파일을 Training폴더의 class1(사과) 폴더에 저장
    zip_file = zipfile.ZipFile(f'{DOWNLOAD_FOLDER_NAME}/{SAVE_DIRECTORY_NAME}/{class1_file}')
    for file in zip_file.filelist:
        if specific_image_name_1 in file.filename:
            zip_file.extract(file.filename, f'{SAVE_DIRECTORY_NAME}/{CLASS_1_NAME}')

# 아래에는 이미지의 종류가 나눠진 폴더에서 이미지의 설명 파일을 읽어서
# 설명 파일을 토대로 이미지의 품질을 각각 good과 bad 폴더에 나눠 담는 코드

apple_img_list = glob.glob(os.path.join(SAVE_DIRECTORY_NAME, classes[0], '*.png'))
mandarine_img_list = glob.glob(os.path.join(SAVE_DIRECTORY_NAME, classes[1], '*.png'))

os.makedirs(os.path.join(SAVE_DIRECTORY_NAME, classes[0], good_img_folder), exist_ok=True) # 첫번째 클래스 폴더에 good 폴더를 생성
os.makedirs(os.path.join(SAVE_DIRECTORY_NAME, classes[0], bad_img_folder), exist_ok=True) # 첫번째 클래스 폴더에 bad 폴더를 생성
os.makedirs(os.path.join(SAVE_DIRECTORY_NAME, classes[1], good_img_folder), exist_ok=True) # 두번째 클래스 폴더에 good 폴더를 생성
os.makedirs(os.path.join(SAVE_DIRECTORY_NAME, classes[1], bad_img_folder), exist_ok=True) # 두번째 클래스 폴더에 bad 폴더를 생성

for apple_img_name in apple_img_list: # 첫번째 클래스(사과) 폴더에 있는 이미지에 대해서 하나씩 설명파일을 읽고, 품질을 분류하는 코드
    img_file_name = os.path.split(apple_img_name)[-1]
    try:
        with open(apple_img_name.replace('.png', '.json'), encoding='utf-8') as f:
            # 이미지의 설명파일은 동일한 파일이름을 가지지만 확장자만 png가 아닌 json으로 설정되어 있습니다.
            # 상기 설정은 AI Hub에서 구축한 방식입니다.
            x = json.load(f)  # 이미지의 설명 파일을 읽는 코드
            if x['cate3'] == '보통': # 설명파일에서 품질을 나타내는 값을 읽어와서 해당 값을 기준으로 이미지를 각각 품질 폴더로 옮기는 코드
                os.rename(apple_img_name, f'{SAVE_DIRECTORY_NAME}/{classes[0]}/{bad_img_folder}/{img_file_name}')
            else:
                os.rename(apple_img_name, f'{SAVE_DIRECTORY_NAME}/{classes[0]}/{good_img_folder}/{img_file_name}')
    except FileNotFoundError:
        os.remove(apple_img_name) # 설명 파일이 없는 이미지의 경우, 해당 이미지를 학습에 이용할 수 없기 때문에 제거
    try:
        os.remove(apple_img_name.replace('.png', '.json')) # 사용한 설명 파일 역시 더 이상 사용하지 않기 때문에 제거
    except:
        pass

for mandarine_img_name in mandarine_img_list: # 두번째 클래스에 대해서 첫번째 클래스의 경우와 동일하게 설명을 읽고 품질을 분류하는 코드
    img_file_name = os.path.split(mandarine_img_name)[-1]
    try:
        with open(mandarine_img_name.replace('.png', '.json'), encoding='utf-8') as f:
            x = json.load(f)
            if x['cate3'] == '보통':
                os.rename(mandarine_img_name, f'{SAVE_DIRECTORY_NAME}/{classes[1]}/{bad_img_folder}/{img_file_name}')
            else:
                os.rename(mandarine_img_name, f'{SAVE_DIRECTORY_NAME}/{classes[1]}/{good_img_folder}/{img_file_name}')
    except FileNotFoundError:
        os.remove(mandarine_img_name)
    try:
        os.remove(mandarine_img_name.replace('.png', '.json'))
    except:
        pass


dummy_file_list = glob.glob(os.path.join(SAVE_DIRECTORY_NAME, '**', '*.json')) # 남아있는 설명 파일들 역시 더이상 사용하지 않기 때문에 제거
for file_name in dummy_file_list:
    os.remove(file_name)