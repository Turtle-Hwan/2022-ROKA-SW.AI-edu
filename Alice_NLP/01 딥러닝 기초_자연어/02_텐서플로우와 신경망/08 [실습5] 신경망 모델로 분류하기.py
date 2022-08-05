'''
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

np.random.seed(100)
tf.random.set_seed(100)

# sklearn에 저장된 데이터를 불러 옵니다.
X, Y = load_iris(return_X_y = True)

# DataFrame으로 변환
df = pd.DataFrame(X, columns=['꽃받침 길이','꽃받침 넓이', '꽃잎 길이', '꽃잎 넓이'])
df['클래스'] = Y

X = df.drop(columns=['클래스'])
Y = df['클래스']

# 학습용 평가용 데이터로 분리합니다
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2, random_state = 42)

# Dataset 형태로 변환합니다.
train_ds = tf.data.Dataset.from_tensor_slices((train_X.values, train_Y))
train_ds = train_ds.shuffle(len(train_X)).batch(batch_size=5)

"""
1. keras를 활용하여 신경망 모델을 생성합니다.
   3가지 범주를 갖는 label 데이터를 분류하기 위해서 마지막 레이어 노드를 아래와 같이 설정합니다.
"""
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, input_dim=4),
    tf.keras.layers.Dense(None, activation=None)
    ])

# 학습용 데이터를 바탕으로 모델의 학습을 수행합니다.
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(train_ds, epochs=100, verbose=2)

# 테스트용 데이터를 바탕으로 학습된 모델을 평가합니다.
loss, acc = model.evaluate(test_X, test_Y)

# 테스트용 데이터의 예측값을 구합니다.
predictions = model.predict(test_X)

# 결과를 출력합니다.
print("테스트 데이터의 Accuracy 값: ", acc)
for i in range(5):
    print("%d 번째 테스트 데이터의 실제값: %d" % (i, test_Y.iloc[i]))
    print("%d 번째 테스트 데이터의 예측값: %d" % (i, np.argmax(predictions[i])))
'''


'''
신경망 모델로 분류하기
이번 실습에서는 Iris 데이터가 주어졌을 때 붓꽃의 종류를 분류하는 신경망 모델을 구현합니다. Iris 데이터는 아래와 같이 꽃받침 길이, 꽃받침 넓이, 꽃잎 길이, 꽃잎 넓이 네 가지 변수와 세 종류의 붓꽃 클래스로 구성되어 있습니다.


분류를 위한 텐서플로우 신경망 모델 함수/메서드

모델 구현 (5개의 범주를 갖는 label 예시)

model = tf.keras.models.Sequential([
tf.keras.layers.Dense(10, input_dim=4),
tf.keras.layers.Dense(5, activation='softmax')
])

분류 모델에서는 마지막 레이어에 분류 데이터의 label 범주의 개수만큼 노드를 설정합니다. 추가로 activation 인자로 ‘softmax’ 를 설정합니다.

학습 방법

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

분류에서는 일반적으로 loss를 ‘sparse_categorical_crossentropy’으로 사용합니다. metrics 인자는 에포크마다 계산되는 평가 지표를 의미합니다. 정확도를 의미하는 ‘accuracy’ 를 입력하면 에포크마다 accuracy를 계산하여 출력합니다.
'''



import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

np.random.seed(100)
tf.random.set_seed(100)

# sklearn에 저장된 데이터를 불러 옵니다.
X, Y = load_iris(return_X_y = True)

# DataFrame으로 변환
df = pd.DataFrame(X, columns=['꽃받침 길이','꽃받침 넓이', '꽃잎 길이', '꽃잎 넓이'])
df['클래스'] = Y

X = df.drop(columns=['클래스'])
Y = df['클래스']

# 학습용 평가용 데이터로 분리합니다
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2, random_state = 42)

# Dataset 형태로 변환합니다.
train_ds = tf.data.Dataset.from_tensor_slices((train_X.values, train_Y))
train_ds = train_ds.shuffle(len(train_X)).batch(batch_size=5)

"""
1. keras를 활용하여 신경망 모델을 생성합니다.
   3가지 범주를 갖는 label 데이터를 분류하기 위해서 마지막 레이어 노드를 아래와 같이 설정합니다.
"""
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, input_dim=4),
    tf.keras.layers.Dense(3, activation='softmax')
    ])

# 학습용 데이터를 바탕으로 모델의 학습을 수행합니다.
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(train_ds, epochs=100, verbose=2)

# 테스트용 데이터를 바탕으로 학습된 모델을 평가합니다.
loss, acc = model.evaluate(test_X, test_Y)  #acc: 추가된 metric 정확도 인자값

# 테스트용 데이터의 예측값을 구합니다.
predictions = model.predict(test_X)

# 결과를 출력합니다.
print("테스트 데이터의 Accuracy 값: ", acc)
for i in range(5):
    print("%d 번째 테스트 데이터의 실제값: %d" % (i, test_Y.iloc[i]))
    print("%d 번째 테스트 데이터의 예측값: %d" % (i, np.argmax(predictions[i])))