- 신경망 이전의 연구  
  얼굴 인식 : 박스 그려서 특정 요소 여부 확인  
  숫자 및 문자 인식 : 필기체 데이터에서, 획들의 구분을 패턴을 정하여 확인  

- 1958년 초기 Perceptron 등장  
- 퍼셉트론 기본 구조

![perceptron structure <출처:https://velog.io/@tobe-honest/%EB%8B%A4%EC%B8%B5-%ED%8D%BC%EC%85%89%ED%8A%B8%EB%A1%A0Multi-layer-Perceptron-MLP>](https://images.velog.io/images/tobe-honest/post/9a2c1497-f2db-4fc6-afd5-e7cd68ecc44a/Perceptrons.jpeg)

![bias <https://blog.naver.com/ucbsong/221423311413>](https://mblogthumb-phinf.pstatic.net/MjAxODEyMjBfMTkw/MDAxNTQ1Mjc5Nzc3NzIx.yM3u7h0fhk0D94uYngVRHpkiwEcQqsJh5kRhO1cUnf0g.ibIVrMGKL7NKCkTEjBIzJli4lpXNb0dPrYPjaRlkdGUg.PNG.ucbsong/neuron_perceptron.png?type=w800)

x1, x2... : 입력 값  
w1, w2... : 가중치 (특정 변수에 대한 영향 높이거나 줄일 때)  
w0 : bias, 상수  
y : 출력 값
y = activation(w0 + w1x1 + w2x2)

- 활성화 함수 (Activation function)  
```python
def activation(x):
    if x>=0:
        return 1
    elif x<0:
        return 0
```

- 퍼셉트론 동작 예시  
x1: 신작 드라마 * w1 : 드라마 시청 욕구로 인한 영향  
x2: 여가시간 * w2 : 여가 시간에 따른 공부하고 싶은 정도  
w0: 의지력  
실제로 공부를 하느냐 0 or 1  

- 퍼셉트론은 선형 분류기로써 데이터 분류 가능하다.

- 선형으로 분류 불가능한 문제는 어떻게??  
1969~ 해결책을 찾는 동안 AI winter 옴..