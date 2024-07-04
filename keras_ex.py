import tensorflow as tf  # tensorflow 라이브러리를 사용하기 위한 코드
from tensorflow import keras
import numpy as np # numpy 라이브러리를 사용하기 위한 코드
# as 키워드는 tensorflow 라는 것을 이제부터는 tf라고 부르겠다 라는 기능을 해줍니다.
import sys
sys.setrecursionlimit(10**8)

X = np.asarray([
    [5, 1], [7, 3], [11, 9], [19, 21], [3, 15], [2, 13], [7, 2], [6, 7] # [남성 고객, 여성 고객]
])
y = np.asarray([13, 23, 49, 101, 51, 43, 20, 33]) # 식당 매출

#  남성 고객이 10명이고 여성 고객이 10명일때 예상 매출은? 50
# 이라는 문제를 해결해 보도록 하겠습니다.

x_input = tf.keras.Input(shape=(2,))
x_hidden = tf.keras.layers.Dense(4)(x_input)  # x_input이라는 입력으로(남성, 여성 고객)부터 4개의 숨겨진 특징을 계산해주는 객체
# ( N x 2 ) x ( 2 x 4 ) -> ( N x 4 )
x_output = tf.keras.layers.Dense(1)(x_hidden)  # 4개의 숨겨진 특징을 통해서 1개의 결과값(식당 매출)을 계산해주는 객체
# ( N x 4 ) x ( 4 x 1 ) -> ( N x 1 )

models = tf.keras.Model(inputs=x_input, outputs=x_output)
# 위에서 설정한 입력과 결과물만 Model객체의 inputs이라는 키워드와 outputs라는 키워드에 넣어주면, 자동으로 중간에 과정을 포함한
# 하나의 딥러닝 모델이 생성됩니다.
# 모델이 계산하는 결과와 저희가 입력하는 결과 즉 예상 매출과 실제 식당 매출의 차이를 최소화 시켜야 좋은 모델이다.
models.compile(loss=tf.keras.losses.MeanSquaredError)  # 그를 위해서 (예상 매출 - 실제 매출) * (예상 매출 - 실제 매출)를 최소화 하도록 모델을 설정

models.fit(X, y, epochs=2000) # 남성, 여성 손님 데이터인 X와 예상 매출 y를 가지고 모델 학습
# 위에서 정한 차이를 최소화 하도록 자동으로 학습
print(models.predict(x=np.asarray([[10, 10]]))) # 예상 매출을 계산하여 실제 매출 50과 비교
