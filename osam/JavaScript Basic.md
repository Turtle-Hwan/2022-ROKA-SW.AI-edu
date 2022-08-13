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
var name = 'Mike';
console.log(name)  // Mike

var name = 'Jane';
console.log(name); // Jane
```
let은 다시 선언하면 오류를 뿜음.  


- 호이스팅 : 스코프 내부 어디서든 변수 선언은 최상위에 선언된 것처럼 행동

var는 선언하기 전에 사용할 수 있다. (호이스팅)
마치 위에서 선언한 것과 같은 효과. 단, 선언은 호이스팅 되나 할당은 호이스팅 되지 않는다.
```js
console.log(name); // undefined (name에 할당된 'Mike'는 호이스팅 되지 않아서 undefined 출력됨)
var name = 'Mike';
```
동일 상황에서 let은 에러를 뿜는다. (ReferenceError)
그런데 let도 호이스팅 된다.  
그러면 왜 에러를 뿜는가? Temporal Dead Zone 때문이다.  
TDZ 안에 있는 변수는 사용할 수 없다. let, const는 TDZ 영향을 받으며, 할당하기 전에 사용할 수 없다는 규칙을 가진다. **이는 코드를 예측 가능하게 해준다.**
```js
console.log(name)   //Temporal Dead Zone 이다. 호이스팅은 되지만 할당되지 않은 변수인 name 사용 불가하여 에러가 난다.
const name = 'Mike' //함수 선언 및 할당
console.log(name)   //사용 가능
```
```js
//let이 호이스팅 되는 것을 보여주는 예시

let age = 30;
function showAge(){
    console.log(age);   //let이 호이스팅 안 된다면 global scope 변수를 받아와 30이 출력되어야 하나, 호이스팅 되므로 에러가 출력된다.
    let age = 20;
}
showAge();
```

<변수의 생성과정>
1. 선언 단계
2. 초기화 단계
3. 할당 단계

var : 
1. 선언 및 초기화 단계 (초기화 : undefined를 할당해주는 단계)
2. 할당 단계  
할당 전에 호출하면 에러 대신 undefined가 나온다

let :
1. 선언 단계 (호이스팅 되면서 선언 이루어짐)
2. 초기화 단계 (실제 코드에 도달해야 초기화가 이루어지므로 그 이전에 접근하면 레퍼런스 에러가 발생함.)
3. 할당 단계  
셋 다 분리되어서 진행된다.

const :
1. 선언 + 초기화 + 할당 (값을 바꿀 수 없기 때문에 동시에 이루어져야 한다.)


var : 함수 스코프  (function-scoped)  
let, const : 블록 스코프 (block-scoped)  
블록 : 함수, if문, for문, while문, try/catch문 등


## 생성자 함수

<객체 리터럴로 객체를 만드는 방식>
```js
let user = {
    name : 'Mike',
    age : 30,
}
```

<생성자 함수로 객체를 만드는 방식>
```js
function User(name, age){
    // this = {} : 빈 객체를 만들고, this에 할당한다.

    this.name = name;
    this.age = age; //this에 프로퍼티를 추가한다.

    // return this; this를 반환한다.
    
    // 첫, 마지막 두 줄은 없으나 실제로 이렇게 동작한다.
}

let user1 = new User('Mike', 30);
let user2 = new User('Jane', 22);
let user3 = new User('Tom', 17);
```
* 생성자 함수는 첫 글자를 대문자로 하는 것이 관례이다.

```js
function User(name, age){
    this.name = name;
    this.age = age;
    this.sayName = function(){
        console.log(this.name);
    }
}

let user5 = new User('Han', 40);
user5.sayName(); // 'Han'   // 여기서 sayName 함수 안의 this가 user5가 됨.
```


## 객체 메소드, 계산된 프로퍼티 (Object methods, Computed property)

<계산된 프로퍼티 (Computed property)>
```js
let a = 'age';
const user = {
    name : 'Mike',
    [a] : 30 // age : 30
}
// user >> {name:"Mike", age: 30}
```
대괄호로 묶어주면, 특정 문자열이 아닌 미리 만들어진 변수에 값이 할당된다. (대괄호 안의 변수에 들어있는 값이 새로운 변수명이 된다.)
```js
const user = {
    [1+4] : 5,
    ["안녕"+"하세요"] : "Hello"
}
// user
// {5:5, 안녕하세요: "Hello"}
```

<객체 메소드 (Methods)>
```js
Object.assign() : 객체 복제 (깊은 복사)

const newUser = Object.assign({}, user); 
// 초기값 {}에 user를 병합시킨다.
// 이때 키가 같다면 덮어쓴다.
```
JS 객체 저장 변수에는 객체를 참조하는 주소값만 들어있음. => 단순히 `const newUser = user;` 이런 식으로 복사하면, newUesr 값을 변경하면 user 값도 변경되는 얕은 복사가 일어난다.

```js
Object.keys() : 키 배열 반환

const user = {
    name : 'Mike',
    age : 30,
    gender : 'male',
}
Object.keys(user);
// ["name", "age", "gender"]
```

```js
Object.values() : 값 배열 반환

const user = {
    name : 'Mike',
    age : 30,
    gender : 'male',
}
Object.values(user);
// ['Mike', 30, 'male']
```

```js
Object.entries() : 키 / 값 배열 반환

const user = {
    name : 'Mike',
    age : 30,
    gender : 'male',
}
Object.entries(user);
/* [
    ["name", "Mike"],
    ["age", 30],
    ["gender", "male"]
   ]
*/
```
```js
Object.fromEntries() : 키 / 값 배열을 객체로 만들어 준다.

const arr = [
    ["name", "Mike"],
    ["age", 30],
    ["gender", "male"]
];
Object.fromEntries(arr);
/*{
    name : 'Mike',
    age : 30,
    gender : 'male',
}*/
```


## 심볼 (symbol)
- 객체 프로퍼티 키는 숫자나 boolean 형으로 만들어도 자동으로 문자형으로 처리된다.
```js
const obj = {
    1 : '11111',
}
Object.keys(obj); // ["1"]
```

`const a = Symbol();` // new를 붙이지 않는다.
- 유일한 식별자를 만들 때 사용한다.


`const id = Symbol('id'); // 설명 붙여주는 것이 나중에 편하다.

