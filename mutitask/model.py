import tensorflow as tf


def get_model(classes, qualities):

    inputs = tf.keras.layers.Input(shape=(128, 128, 3))
    hidden = tf.keras.layers.Conv2D(32, 5, 2, padding='same')(inputs) # 이미지에 존재하는 직선이나 곡선과 같은 특징을 얻어 낸다.
    hidden = tf.keras.layers.Activation('swish')(hidden)

    hidden = tf.keras.layers.Conv2D(64, 3, 2, padding='same')(hidden) # 이미지에 존재하는 직선이나 곡선의 특징을 활용하여 보다 복잡한 특징을 얻어낸다.
    hidden = tf.keras.layers.Activation('swish')(hidden)

    hidden = tf.keras.layers.Conv2D(128, 3, 2, padding='same')(hidden) # 이전에 뽑아낸 복잡한 특징으로 더 복잡한 특징을 뽑아낸다.
    hidden = tf.keras.layers.Activation('swish')(hidden)
    gap_hidden_1 = tf.keras.layers.GlobalAveragePooling2D()(hidden)  # 뽑은 특징을 활용하기 편한 형태로 변환한다.

    hidden = tf.keras.layers.Conv2D(256, 3, 2, padding='same')(hidden) # 이전에 뽑아낸 복잡한 특징으로 더 복잡한 특징을 뽑아낸다.
    hidden = tf.keras.layers.Activation('swish')(hidden)


    gap_hidden_2 = tf.keras.layers.GlobalAveragePooling2D()(hidden) # 뽑은 특징을 활용하기 편한 형태로 변환한다.
    class_output = tf.keras.layers.Dense(len(classes), activation='softmax', name='class')(gap_hidden_2) # 뽑은 특징을 활용해서 classes_name의 각각 성분일 확률이 얼마인지 반환해준다.

    quality_hidden_1 = tf.keras.layers.Dense(128, activation='swish')(gap_hidden_1) # 뽑은 특징을 활용해서 classes_name의 각각 성분일 확률이 얼마인지 반환해준다.
    quality_hidden_2 = tf.keras.layers.Dense(128, activation='swish')(gap_hidden_2) # 뽑은 특징을 활용해서 classes_name의 각각 성분일 확률이 얼마인지 반환해준다.
    quality_hidden = tf.keras.layers.Average()([quality_hidden_1, quality_hidden_2])
    quality_output = tf.keras.layers.Dense(len(qualities), activation='softmax', name='quality')(quality_hidden) # 뽑은 특징을 활용해서 classes_name의 각각 성분일 확률이 얼마인지 반환해준다.
    # activation에 설정된 softmax 경우 각 성분들의 합이 1이되도록 변환해주는 수학 함수으로
    # classes_name이 만약 ['apple', 'mandarine'] 이면 모델 반환이 [0.9, 0.1] 과 같이 합이 1이되도록 값을 변경해주는 함수

    return tf.keras.Model(inputs, [class_output, quality_output])