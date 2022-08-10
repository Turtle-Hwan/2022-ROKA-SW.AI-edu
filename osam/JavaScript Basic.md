# JavaScript Basic

## 변수
## 자료형
## alert, prompt, confirm
prompt : 사용자 입력을 받을 수 있는 모달 창 띄움.

confirm : 확인 / 취소 버튼 있으며 메세지 지정 가능한 모달 창 띄움.

## 형변환
## 기본 연산자
## 비교 연산자, 조건문
## 논리 연산자
## 반복문
## switch문
## 함수의 기초

## 함수 표현식, 화살표 함수
함수 선언문: 일반적인 함수 선언
```js
function sayHello(){
    console.log('Hello');
}
```

함수 표현식: 변수에다 함수를 집어 넣는 것.
```js
let sayHello = function(){
    console.log('Hello')
}
```

- 함수 선언문은 어디서든 함수 호출해서 사용 가능하다.
=> js는 실행 전 코드의 모든 함수 선언문을 찾아서 미리 실행해 놓는다. 이를 호이스팅이라고 한다. (다만 실제로 코드 위치가 올라가는 것은 아님.)

- 함수 표현식은 코드에 도달하면 해석된다. 따라서 그 이후에 함수를 호출할 수 있다.


화살표 함수 : 
```js
let add = function(num1, num2){
    return num1 + num2;
}

let add = (num1, num2) => {
    return num1 + num2;
}

//리턴문만 있다면 일반 괄호로 바꿀 수 있다.
let add = (num1, num2) => (num1+num2;)

//리턴문이 한 줄이라면 괄호도 생략할 수 있다.
let add = (num1, num2) => num1+num2;

//받는 인자가 하나라면 괄호 생략 가능.
let sayHello = name => `Hello, ${name}`;
```


## 객체 (Object)
객체는 중괄호로 작성하고 키와 값으로 구성된 property가 들어간다. property는 쉼표로 구분한다.
```js
const superman = {
    name:'clark',
    age:33,
}
```

- 접근
```js
superman.name // 'clark'
auperman['age'] // 33
```

- 추가
```js
superman.gender = 'male';
superman['hairColor'] = 'black';
```

- 삭제
```js
delete superman.hairColor;
```

### Object - 단축 프로퍼티
```js
const name = 'clark'
const age = 33;
const superman = {
    name,   // name = name
    age,    // age = age
    gender:'male',
}

//없는 프로퍼티를 사용하려 하면 에러가 안난다.
superman.birthDay; // undefined

//이때 in 연산자 활용하면 포함하는지 알 수 있다.
'birthDay' in superman; // false
```

### for...in 반복문
```js
//객체 순회하면서 모든 요소 얻어오기 가능.
for(let key in superman) {
    console.log(key)
    console.log(superman[key])
}
```


## 객체(Object) - method, this
method : 객체 프로퍼티로 할당 된 함수
```js
const superman = {
    name:'clark',
    age:33,
    fly:function() {
        console.log('날아갑니다.')
    }
    //function 키워드 생략도 가능하다.
    //fly(){
    //    console.log('날아갑니다.')
    //}
}
```


this : 
this는 런타임에 결정된다.
```js
const user = {
    name:'Mike',
    sayHello:function(){
        cosole.log(`Hello, I'm ${this.name}`);  //user.name으로 호출하면 문제가 생길 수 있음.
    }
}
```
```js
sayHello:function(){
    cosole.log(`Hello, I'm ${this.name}`);
}
}
let boy = {
    name:'Mike',
    sayHello,
}
let girl = {
    name:'Jane',
    sayHello,
}

boy.sayHello(); // Hello, I'm Mike
girl.sayHello();// Hello, I'm Jane

//이때, sayHello를 화살표 함수로 선언했다면 동작이 전혀 달라지게 된다.
```
- 화살표 함수는 일반 함수와는 달리 자신만의 this를 가지지 않는다. 화살표 함수 내부에서 this를 사용하면, 그 this는 외부에서 값을 가져 온다.

```js
let boy = {
    name:'Mike',
    sayHello:()=>{
        console.log(this); //이때 this는 boy가 아니라, 전역객체를 가리킨다. JS에서는 window, nodsJS에서는 global
    }
}
```


## 배열
순서있는 리스트
```js
let students = ['철수', '영희', '영수']
```
배열은 문자 뿐 아니라 숫자, 객체, 함수 등고 포함 가능하다.

length : 배열 길이 구하기. 
```js
students.length // 3
```
push() : 배열 끝에 원소 추가  
pop() : 배열 끝 원소 제거

shift() : 배열 앞에 원소 제거 (한번에 추가 가능) 
unshift() : 배열 앞에 원소 추가 (한번에 추가 가능)
```js
days.unshift('금', '토', '일');
console.log(days) // ['금','토','일','월','화','수'];
```

배열을 쓰는 가장 큰 이유는 반복을 위해서.

### for ... of (배열은 for...in의 단점이 많기에 권장하지 않는다.)
```js
let days = ['월','화','수'];
for (let day of days){
    console.log(day)
}
//for문보다 간단하지만 index를 못 얻는다는 단점.
```


# JavaScript Intermediate
## 변수, 호이스팅, TDZ(Temporal Dead Zone)
변수 : let, const, var
var는 한 번 선언된 변수를 다시 선언 가능하다.
```js
var
```