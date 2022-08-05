'''
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

np.random.seed(100)
tf.random.set_seed(100)

# 데이터를 DataFrame 형태로 불러 옵니다.
df = pd.read_csv("data/Advertising.csv")

# DataFrame 데이터 샘플 5개를 출력합니다.
print('원본 데이터 샘플 :')
print(df.head(),'\n')

# 의미없는 변수는 삭제합니다.
df = df.drop(columns=['Unnamed: 0'])

X = df.drop(columns=['Sales'])
Y = df['Sales']

# 학습용 테스트용 데이터로 분리합니다.
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.3)

# Dataset 형태로 변환합니다.
train_ds = tf.data.Dataset.from_tensor_slices((train_X.values, train_Y))
train_ds = train_ds.shuffle(len(train_X)).batch(batch_size=5)

# keras를 활용하여 신경망 모델을 생성합니다.
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, input_shape=(3,)),
    tf.keras.layers.Dense(1)
    ])

# 학습용 데이터를 바탕으로 모델의 학습을 수행합니다.
model.compile(loss='mean_squared_error', optimizer='adam')
history = model.fit(train_ds, epochs=100, verbose=2)

"""
1. evaluate 메서드를 사용하여 테스트용 데이터의 loss 값을 계산합니다.
"""
loss = model.evaluate(None, None, verbose=0)

"""
2. predict 메서드를 사용하여 테스트용 데이터의 예측값을 계산합니다.
"""
predictions = model.predict(None)

# 결과를 출력합니다.
print("테스트 데이터의 Loss 값: ", loss)
for i in range(5):
    print("%d 번째 테스트 데이터의 실제값: %f" % (i, test_Y.iloc[i]))
    print("%d 번째 테스트 데이터의 예측값: %f" % (i, predictions[i][0]))
'''

'''
텐서플로우를 활용하여 신경망 구현하기 - 모델 평가 및 예측
[실습3]에 이어서 이번 실습에서는 학습된 신경망을 모델을 평가하고 예측해보겠습니다.

텐서플로우를 이용해 신경망 모델을 평가 및 예측을 위한 함수/메서드

평가 방법

model.evaluate(X, Y)

evaluate() 메서드는 학습된 모델을 바탕으로 입력한 feature 데이터 X와 label Y의 loss 값과 metrics 값을 출력합니다. 이번 실습에서는 metrics 를 complie에서 설정하지 않았지만, 분류에서는 일반적으로 accuracy를 사용하여 evaluate 사용 시, 2개의 아웃풋을 리턴합니다.

예측 방법

model.predict(X)

X 데이터의 예측 label 값을 출력합니다.
'''

import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

np.random.seed(100)
tf.random.set_seed(100)

# 데이터를 DataFrame 형태로 불러 옵니다.
df = pd.read_csv("data/Advertising.csv")

# DataFrame 데이터 샘플 5개를 출력합니다.
print('원본 데이터 샘플 :')
print(df.head(),'\n')

# 의미없는 변수는 삭제합니다.
df = df.drop(columns=['Unnamed: 0'])

X = df.drop(columns=['Sales'])
Y = df['Sales']

# 학습용 테스트용 데이터로 분리합니다.
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.3)

# Dataset 형태로 변환합니다.
train_ds = tf.data.Dataset.from_tensor_slices((train_X.values, train_Y))
train_ds = train_ds.shuffle(len(train_X)).batch(batch_size=5)

# keras를 활용하여 신경망 모델을 생성합니다.
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, input_shape=(3,)),
    tf.keras.layers.Dense(1)
    ])

# 학습용 데이터를 바탕으로 모델의 학습을 수행합니다.
model.compile(loss='mean_squared_error', optimizer='adam')
history = model.fit(train_ds, epochs=100, verbose=2)

"""
1. evaluate 메서드를 사용하여 테스트용 데이터의 loss 값을 계산합니다.
"""
loss = model.evaluate(test_X, test_Y, verbose=0)    #evaluate 함수 자체가 받은 x, y 인자값을 tensor로 변환해서 넣어줌.

"""
2. predict 메서드를 사용하여 테스트용 데이터의 예측값을 계산합니다.
"""
predictions = model.predict(test_X)

# 결과를 출력합니다.
print("테스트 데이터의 Loss 값: ", loss)
for i in range(5):
    print("%d 번째 테스트 데이터의 실제값: %f" % (i, test_Y.iloc[i]))
    print("%d 번째 테스트 데이터의 예측값: %f" % (i, predictions[i][0]))
