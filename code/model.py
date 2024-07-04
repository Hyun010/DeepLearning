import tensorflow as tf
import json


def get_model(classes):

    inputs = tf.keras.layers.Input(shape=(64, 64, 3))
    hidden = tf.keras.layers.Conv2D(filters=64, kernel_size=7, strides=2, padding='same')(inputs)
    # 위의 layer는 이미지에 존재하는 직선이나 곡선과 같은 특징을 얻어 내는 역할을 합니다.
    # filters : inputs에서 부터 뽑아낼 특징 수
    # kernel_size : 특징을 뽑아낼 일부분의 크기, 한장의 이미지를 kernel_size 만큼의 크기를 가진 작은 이미지로 잘라서 특징을 추출
    # strides : 7x7로 이미지를 자를 때, 2칸씩 옴겨가며 자름 -> 겹치는 부분이 있게 자름
    # (N, 64, 64, 1) -> (N, 32, 32, 16)

    # 추후 활용 방안
    # 현재는 이미지 각각 위치에 직선 등의 특징을 16개를 추출하게 되는데, 모델 성능이 만족스럽지 못한 경우
    # 16의 값을 보다 큰 수로 변경하면, 보다 많은 특징을 뽑아내는 모델을 학습 할 수 있습니다.
    # 하지만 보다 많은 특징을 뽑아내기 위해서는 결국 보다 많은 양의 데이터가 학습에 필요하게 됩니다.

    hidden = tf.keras.layers.Activation('swish')(hidden)
    # swish라는 이름을 가진 활성화 함수를 적용용

    hidden = tf.keras.layers.Conv2D(128, 5, 2, padding='same')(hidden)
    # 이미지에 존재하는 직선이나 곡선 등의 지난번 레이어에서 추출한 특징을 활용하여 보다 복잡한 특징을 얻어낸다.
    # 같은 방법으로 모델의 성능을 향상시키기 위해서 32
    hidden = tf.keras.layers.Activation('swish')(hidden)

    hidden = tf.keras.layers.Conv2D(256, 3, 2, padding='same')(hidden) # 이전에 뽑아낸 복잡한 특징으로 더 복잡한 특징을 뽑아낸다.
    hidden = tf.keras.layers.Activation('swish')(hidden)
    
    hidden = tf.keras.layers.Conv2D(512, 3, 2, padding='same')(hidden) # 이전에 뽑아낸 복잡한 특징으로 더 복잡한 특징을 뽑아낸다.
    hidden = tf.keras.layers.Activation('swish')(hidden)

    hidden = tf.keras.layers.GlobalAveragePooling2D()(hidden) # 뽑은 특징을 활용하기 편한 형태로 변환한다.
    hidden = tf.keras.layers.Dense(len(classes), activation='softmax')(hidden) # 뽑은 특징을 활용해서 classes_name의 각각 성분일 확률이 얼마인지 반환해준다.
    # activation에 설정된 softmax 경우 각 성분들의 합이 1이되도록 변환해주는 수학 함수으로
    # classes_name이 만약 ['apple', 'mandarine'] 이면 모델 반환이 [0.9, 0.1] 과 같이 합이 1이되도록 값을 변경해주는 함수

    return tf.keras.Model(inputs, hidden)