# 01 1주차 Node.js 소개와 설치
## 01
---

## Node.js란?
Node.js는 서버사이드 JS, V8 기반 구성  

이벤트 기반 개발 가능, Non-Blocking I/O 지원하기 때문에 비동기식 프로그래밍 가능 => I/O 부하가 심한 대규모 서비스 개발에 적합.

JS 표준라이브러리 프로젝트인 CommonJS 스펙 따름.

Python의 Twisted, Perl Object Environment, C의 libevent, Ruby의 EventMachine 등 비동기 프로그래밍 모델 존재.

### 노드의 탄생 배경
2009년 라이언 달이 고안.

다수의 연결을 효율적으로 관리하고, 비용을 최소화하는 네트워크 소프트웨어를 개발하는 편리한 방법 제공 위해 개발됨.

최초의 네트워크 (서버사이드) 개발은 CGI라 해서 펄 등의 스크립트를 이용했다. 이후에는 ASP, JSP, PHP 등 서버사이드 웹앱 개발 전용 스크립트 언어가 나왔다.

웹 앱을 개발한다 하면 일반적으로 아파치 같은 웹 서버에서 동작하게 된다. 이때 어떤 클라이언트가 웹 서버로 연결을 요청하면 일정한 메모리 공간을 사용하여 새로운 쓰레드를 생성한다. 
이런 형태로 웹 앱을 개발하여 서비스를 제공하면 더 많은 사용자를 지원하기 위해 사업자는 더 많은 서버를 추가해야 한다. 이는 서버 구매 비용에 운영 비용, 신규 트래픽 비용, 인건비 등 여러 비용을 발생시킨다는 문제가 있다. 여러 대의 서버를 사용하더라도 사용자 입장에서는 하나의 서버에 접속하는 경험을 주어야 하므로 모든 서버는 같은 데이터를 동기화 해야 한다는 문제도 발생한다.

노드는 서버에서 클라이언트로부터의 요청, 연결을 처리하는 방법을 새로운 컨셉으로 변경하여 이 문제를 해결한다. 기존에는 각 연결마다 새로운 쓰레드를 생성하고, 이에 따른 메모리를 할당하여 사용자 요청을 처리했다면, 노드에서는 각 연결이 하나의 이벤트로 노드 엔진에서 처리된다.

### 노드를 사용하는 서비스들
월마트 : 하이브리드 앱 스타일로 구현, 기능 대부분은 노드를 통해 서버 사이드에서 작동

링크드인 : 노드와 mongoDB 이용, 원래 Ruby On Rails로 돌릴 땐 15대 서버에서 15개 인스턴스로 돌리다, 노드로는 두 배의 트래픽을 4개의 인스턴스로 운영 가능하다고 밝힘.
노드로 VNC 클라이언트 구현??!

Cloud9 IDE : 가장 널리 쓰이는 웹 기반 IDE, 노드로 개발됨.




## 02
---
## 이벤트 기반 비동기 방식
노드가 성능이 뛰어난 이유 : 비동기 이벤트 기반 아키텍처 / 구글의 V8 JS 엔진 이용

### 쓰레드 기반 vs 비동기 이벤트 기반
지금까지 대부분의 애플리케이션은 Blocking I/O를 사용했고, 이 때문에 멀티 쓰레드를 사용할 수밖에 없었다. 멀티 쓰레드는 개발자 입장에서 직관적이고 멀티 태스킹을 위해서 어쩔 수 없는 선택이지만, 네트워크에서 동시에 대규모 요청을 처리하는 데는 부적절하다.

### Blocking I/O
Blocking I/O : 하나의 프로세스가 어떤 자원을 사용하고자 할 때 그 자원을 다른 프로세스가 점유하고 있다면, 사용을 마칠 때까지 기다려야 한다는 것.

애플리케이션이 운영체제의 커널에게 파일을 읽기 위해 시스템 콜이라는 형태로 요청을 보내면 커널은 파일을 읽고, 애플리케이션은 커널이 파일을 다 읽을 때까지 기다려야 한다. 이 상태가 Blocked이며 애플리케이션은 아무것도 하지 않는다.

### 멀티 쓰레드
일반적으로 하나의 프로세스가 하나의 요청에 대응하고 일을 처리한다. 만약 웹서버처럼 다수의 요청이 들어오면 멀티 쓰레드 개념을 사용한다.

CPU의 시분할이라는 개념으로 설명될 수 있으며, 하나의 CPU를 여러 프로세스 또는 쓰레드가 시간을 나누어 동작하도록 함으로써 마치 CPU를 공유하여 사용하는 것과 같은 효과를 낸다.


# 02 1주차 기본 모듈과 Node.js 기초
## 01
---
### 노드의 모듈 개념
### 전역 객체 : Global
### OS 모듈
OS 모듈은 실제 개발에서 많이 사용되는 모듈은 아니지만 운영체제와 시스템의 정보를 가져올 수 있는 모듈입니다. CPU나 메모리, 디스크 용량이 얼마나 남았는지 확인이 필요할 때 사용합니다. 즉 사용자가 실행하는 환경에 따라서 값이 다르게 나옵니다.
os.tmpdir() : 임시 저장 폴더의 위치
os.endianness() : CPU의 endianness(BE 또는 LE)
os.hostname() : 호스트(컴퓨터) 이름
os.type() : 운영체제 이름
os.platform() : 운영체제 플랫폼
os.arch() : 운영체제 아키텍처
os.release() : 운영체제 버전
os.uptime() : 운영체제가 실행된 시간
os.loadavg() : 로드 에버리지 정보를 담은 배열
os.totalmem() : 시스템의 총 메모리
os.freemem() : 시스템의 가용 메모리
os.cpus() : CPU의 정보를 담은 객체. CPU의 세부 정보를 반환합니다.
os.networkInterfaces() : 네트워크 인터페이스 정보를 담은 배열


### Utility 모듈
Utility 모듈은 node.js의 보조적인 기능 중 유용한 기능만을 모아놓은 모듈입니다. https://nodejs.org/api/util.html

util.format(format, [...]) : console.log() 메소드와 비슷한 기능이지만 console.log()는 화면에 출력하고 util.format은 문자열로 반환합니다. printf와 같은 형식으로 첫 아규먼트를 사용해서 포맷팅된 문자열을 반환합니다. 플레이스 홀더는 다음과 같은 아규먼트의 값으로 대체됩니다.
%s : 문자열
%d : 숫자(정수부터 소수까지 표현 가능)
%j : JSON
% : 퍼센트 기호('%'). 이 기호는 플레이스홀더를 사용하지 않습니다.
util.debug(string) : 프로그램의 실행을 멈추고 즉각적으로 string을 출력합니다.
util.log(string) : 타임스탬프 시간과 함께 string을 출력합니다.
util.isArray(object) : 주어진 object가 Array이면 true, 아니면 false를 리턴합니다.
util.isRegExp(object) : 주어진 object가 RegExp이면 true, 아니면 false를 리턴합니다.
util.isDate(object) : 주어진 object가 Date이면 true, 아니면 false를 리턴합니다.
util.isError(object) : 주어진 object가 Error이면 true, 아니면 false를 리턴합니다.

### File System 모듈
파일 처리와 관련된 작업을 하는 모듈로, 보통 FileSystem을 줄여서 fs 모듈이라고 줄여 부릅니다. 노드에서 가장 중요한 모듈 중 하나입니다. 메소드가 무척 많으므로 여기서는 기초인 파일 읽기와 쓰기 기능을 살펴보겠습니다. https://nodejs.org/api/fs.html

대부분의 메소드들이 동기/비동기로 나뉘는데, Sync라는 이름이 붙어있는 메소드가 동기방식을 사용한다고 보면 됩니다.

동기적 읽기 방식을 사용하면 파일을 읽으면서 다른 작업을 동시에 할 수 없습니다. 하지만 비동기적으로 읽으면 파일을 읽으면서 다른 작업도 동시에 수행할 수 있고, 파일을 다 읽으면 매개변수 callback으로 전달한 함수가 호출됩니다. 비동기 형식은 항상 마지막 인수가 수행 완료 시 호출할 콜백 함수로 작성되어야 합니다.

주로 비동기적 형식을 많이 사용하지만, 서버 시작 시 설정 파일을 읽는 작업과 같이 동기적 형식이 더 적절한 경우도 있습니다. [options]에는 보통 인코딩 방식을 쓰며, 웹에서는 UTF-8을 주로 사용합니다.

fs.readFile(filename, [options], callback) : filename의 파일을 [options]의 방식으로 읽은 후 callback으로 전달된 함수를 호출합니다. (비동기적) 
fs.readFileSync(filename, [options]) : filename의 파일을 [options]의 방식으로 읽은 후 문자열을 반환합니다.(동기적)
fs.writeFile(filename, data, [options], callback) : filename의 파일에 [options]의 방식으로 data 내용을 쓴 후 callback 함수를 호출합니다.(비동기적) 
fs.writeFileSync(filename, data, [options]) : filename의 파일에 [options]의 방식으로 data 내용을 씁니다.(동기적)

동기적 방식에서는 자바스크립트에서 예외처리를 할 때 일반적으로 써주는 방식인 try~catch 구문으로 처리합니다. 쓰기도 마찬가지로 try catch 구문으로 써주면 됩니다.

이제 비동기적 방식을 알아봅시다. 비동기적 방식에서는 예외가 발생하면 callback 함수의 매개변수 err에 전달되므로, 따로 try~catch 구문을 사용할 필요가 없습니다.



### Event 모듈
노드의 많은 객체는 이벤트를 발생시키는데, 이러한 객체들은 바로 events.EventEmitter라는 인스턴스를 이용하고 있습니다. 이벤트 이름은 띄어쓰기 대신 대문자로 문자를 구분하는 "카멜(낙타)표기법"을 사용하는 것이 정석이지만 강제는 아닙니다.  https://nodejs.org/api/events.html

Node.js에서는 이벤트 모듈과 EventEmitter 클래스가 내장되어 있는데, 이를 사용하여 이벤트와 이벤트 핸들러를 연동시킬 수 있습니다.

이벤트를 활용하는 객체에는 해당 이벤트가 발생할 때 대응하여 동작하는 콜백 함수를 가지는데, 이러한 함수를 이벤트 리스너라고 부르기도 합니다. 이벤트 모듈을 사용하려면 require() 메소드를 이용하여 로드하고, 그 객체를 통해 EventEmitter 클래스를 로드하여 사용하는 것이 일반적입니다.


events 객체의 메소드
emitter.addListener(event, listener) : on() 메소드와 같습니다. 이벤트를 생성하는 메소드입니다.
emitter.on(event, listener) : addListener()과 동일합니다. 이벤트를 생성하는 메소드입니다.
emitter.once(event, listener) : 이벤트를 한 번만 연결한 후 제거합니다.
emitter.removeListener(event, listener) : 특정 이벤트의 특정 이벤트 핸들러를 제거합니다. 이 메소드를 이용해 리스너를 삭제하면 리스너 배열의 인덱스가 갱신되니 주의해야 합니다.
emitter.removeAllListeners([event]) : 모든 이벤트 핸들러를 제거합니다.
emitter.setMaxListeners(n) : n으로 한 이벤트에 최대허용 개수를 정해줍니다. node.js는 기본값으로 한 이벤트에 10개의 이벤트 핸들러를 작성할 수 있는데, 11개 이상을 사용하고 싶다면 n값을 넘겨주면 됩니다. n값으로 0을 넘겨 주면 연결 개수 제한이 사라집니다.
emitter.emit(eventName[, ...args]) : 이벤트를 발생시킵니다.


02 1주차 기본 모듈과 Node.js 기초
Event 모듈
노드의 많은 객체는 이벤트를 발생시키는데, 이러한 객체들은 바로 events.EventEmitter라는 인스턴스를 이용하고 있습니다. 이벤트 이름은 띄어쓰기 대신 대문자로 문자를 구분하는 "카멜(낙타)표기법"을 사용하는 것이 정석이지만 강제는 아닙니다. 모든 메소드는 API 문서에서 볼 수 있으며, 여기서는 이벤트를 발생시키고 삭제하는 기본적인 메소드에 관해서만 알아보겠습니다. Node.js에서는 이벤트 모듈과 EventEmitter 클래스가 내장되어 있는데, 이를 사용하여 이벤트와 이벤트 핸들러를 연동시킬 수 있습니다.

이벤트를 활용하는 객체에는 해당 이벤트가 발생할 때 대응하여 동작하는 콜백 함수를 가지는데, 이러한 함수를 이벤트 리스너라고 부르기도 합니다. 이벤트 모듈을 사용하려면 require() 메소드를 이용하여 로드하고, 그 객체를 통해 EventEmitter 클래스를 로드하여 사용하는 것이 일반적입니다.



events 객체의 메소드
emitter.addListener(event, listener) : on() 메소드와 같습니다. 이벤트를 생성하는 메소드입니다.
emitter.on(event, listener) : addListener()과 동일합니다. 이벤트를 생성하는 메소드입니다.
emitter.once(event, listener) : 이벤트를 한 번만 연결한 후 제거합니다.
emitter.removeListener(event, listener) : 특정 이벤트의 특정 이벤트 핸들러를 제거합니다. 이 메소드를 이용해 리스너를 삭제하면 리스너 배열의 인덱스가 갱신되니 주의해야 합니다.
emitter.removeAllListeners([event]) : 모든 이벤트 핸들러를 제거합니다.
emitter.setMaxListeners(n) : n으로 한 이벤트에 최대허용 개수를 정해줍니다. node.js는 기본값으로 한 이벤트에 10개의 이벤트 핸들러를 작성할 수 있는데, 11개 이상을 사용하고 싶다면 n값을 넘겨주면 됩니다. n값으로 0을 넘겨 주면 연결 개수 제한이 사라집니다.
emitter.emit(eventName[, ...args]) : 이벤트를 발생시킵니다.


이벤트 생성(이벤트 핸들러 연결)
이벤트를 추가하려면, emitter에 이벤트를 연결할 객체, event에 이벤트 이름, listener에 이벤트 핸들러를 작성하면 됩니다. addlistener() 메소드와 on() 메소드는 서로 같으니 둘 중 익숙한 것을 사용하면 됩니다. 간단한 예제를 통해 이벤트 생성에 대해 알아봅시다.

이벤트 제거
addlistener() 메소드나 on() 메소드를 통해 연결된 이벤트 핸들러를 제거하기 위해 사용됩니다. removeListener()를 사용하면 특정 이벤트 리스너를 제거할 수 있고,  removeAllListeners() 를 사용하면 모든 이벤트 리스너를 제거합니다. removeAllListeners([eventname]) 을 사용하면 해당 이벤트의 모든 리스너를 제거할 수 있습니다.


### 노드에서의 상속
노드는 자바스크립트를 기본으로 만들어졌기 때문에 자바스크립트와 동일하게 상속할 수 있지만, 좀 더 편리하게 상속할 수 있도록 util 모듈을 통해 별도의 메소드를 지원하고 있습니다. 먼저 전통적인 자바스크립트 상속 방법을 살펴본 후, 노드의 util 모듈에서 지원하는 상속방법을 알아봅시다.

```js
function Foo() {
    // 코드
}

Foo.prototype = {
    bar: function() {
        console.log('Foo_bar 실행');
    }
};
```
위의 코드는 bar()  메소드를 가진 Foo 객체를 생성하는 코드입니다. Foo를 상속받아 Bar 객체를 생성하는 코드를 아래에서 살펴봅시다.


```js
function Bar() {
}

Bar.prototype = Object.create(Foo.prototype);

Bar.prototype.baz = function() {
    console.log('Bar_baz 실행');
};

Foo.prototype.bar();
Bar.prototype.bar();
Bar.prototype.baz();
```
Foo 객체의 원형을 상속받은 Bar 객체는 Foo의 bar() 메소드를 사용할 수 있게 되었습니다. 


util.inherits() 메소드를 이용한 상속
하지만, 노드에서 지원되는 util.inherits() 메소드를 이용하면 더 쉽고 간단하게 상속할 수 있습니다. 커다란 차이는 없지만, 작성해야 하는 코드의 양이 조금 줄어들고, Bar가 Foo를 상속받았다는 것을 명확하게 보이게 해줍니다.

```js
var util = require('util');

function Bar() {
}

util.inherits(Bar, Foo);

Bar.prototype.baz = function() {
	console.log('Bar_baz 실행');
};

Foo.prototype.bar();
Bar.prototype.bar();
Bar.prototype.baz();
```


# 03
# 1주차 확장모듈 - npm 활용하기
## npm 소개 및 설치
npm은 Node.js에서 사용 가능한 모듈들을 패키지화시켜 모아놓은 것으로, npm이란 이름은 "Node Package Manager"의 약자입니다. 더 정확히는, 다른 커맨드라인 유틸리티로부터 이름을 따왔지만 이 부분은 중요하지 않으니 저렇게만 알아두시면 됩니다. 아이작 슐레터(Isaac Z, Schlueter)가 만든 노드의 모듈 패키지 관리 도구로써, 확장 모듈의 관리를 쉽게 하게 도와줍니다.

이를 통해 웹에서 필요로 하는 특정 기능들을 일일이 개발하지 않아도 이미 누군가가 만들어 올려놓은 모듈을 다운받기만 하면 되므로, 개발을 쉽게 할 수 있어서 노드가 빠르게 인기를 끄는 것에 도움을 주었습니다. 또한 npm 역시 Node.js의 급격한 인기로 인해 빠르게 성장하여 세계 최대의 패키지 저장소가 되었습니다.

과거에는 Node.js를 설치한 후 npm을 따로 설치해야 했지만, 현재는 Node.js를 설치만 해도 자동으로 npm이 설치되므로 편리합니다. 노드의 기본 API를 이용하여 특정한 기능을 더 쉽게 구현할 수 있도록 추상화한 API를 제공하기 때문에 npm은 노드 개발에서 없어서는 안 될 존재라고 할 수 있습니다.

노드의 확장 모듈과 npm
노드의 기본 모듈은 기본적인 API만을 제공합니다. 물론 기본 모듈만 사용하더라도 웬만한 애플리케이션은 개발할 수 있습니다. 클라이언트 자바스크립트 개발을 할 때 직접 작성한 자바스크립트, 즉 네이티브 자바스크립트로만 개발하지 않고, jQuery나 프로토타입을 사용하는 것과 유사하다고 할 수 있겠지요.

하지만 유명한 확장 모듈은 이미 많은 개발자가 사용하여 검증되었으므로 이러한 모듈들을 이용하면 프로젝트의 생산성을 극대화할 수 있습니다. 단, 확장 모듈을 사용하여 개발한 결과물을 배포할 때는 소스가 의존하는 확장 모듈도 함께 설치되어야 합니다. 그래야만 다른 협업 개발자들이나 사용자들이 개발 환경이나 구동 환경을 설정할 때 어려움이 없습니다.

또한, 이렇게 의존하는 확장 모듈이 업데이트되면 이에 따른 확장 모듈의 관리가 필요한데, npm이 이러한 역할을 합니다. 자바 개발자는 메이븐, 리눅스 사용자는 rpm, apt-get 등을 떠올리면 됩니다.

## 확장모듈 설치
글로벌 설치(전역 설치)
확장 모듈을 글로벌로 설치하면 {prefix}/lib/node_modules 에 노드 모듈을 설치하고 모듈을 구성하는 파일 중 실행과 관련된 파일들은 {prefix}/bin 에 설치합니다. 그리고 매뉴얼 페이지는 {prefix}/share/man 에 설치합니다. 여기서 {prefix}는 기본적으로 /usr/local 입니다. (윈도우라면 디렉터리 구조가 다를 수 있습니다.)

글로벌로 설치하는 확장 모듈은 주로 명령줄 도구처럼 사용하는 것입니다. 명령줄에서 사용하는 모듈은 노드로 작성한 소스와는 의존성이 없는데, 주로 개발의 편의성이나 지속적인 서비스를 위한 도구 등이 이러한 형태입니다. 이러한 확장 모듈은 특정 프로젝트에서만 사용하는 것이 아니므로 주로 글로벌로 설치하여 사용하는 것이 좋습니다. 확장 모듈 중 nodemon이나 express와 같은 모듈을 글로벌로 설치하여 사용하는 것을 권장합니다. 즉, 셸에서 커맨드라인처럼 사용하고 싶은 모듈은 전역으로 설치하고, 어떤 한 프로젝트에서 필요한 모듈은 지역 설치를 하는 것을 권장합니다. 전역 변수 대신 지역 변수를 권장하는 것처럼, 필요한 경우가 아니라면 모듈 역시 전역 설치보다는 지역 설치가 좋습니다. 


로컬 설치(지역 설치)
확장 모듈을 로컬로 설치하면 현재 디렉터리에 패키지를 설치합니다. 확장 모듈을 로컬로 설치하면 현재 디렉터리에 패키지를 설치합니다. 노드 모듈은 ./node_modules 에 설치하고, 실행 관련 파일들은 ./node_modules/bin/ 에 설치하며 매뉴얼 페이지를 설치하지 않습니다.

소스 코드에서 require() 메소드를 통해 사용하는 형태로 특정 애플리케이션에 국한되어 사용하는 경우가 많은 확장 모듈일 경우 로컬 설치 형태를 사용하는 것이 좋습니다. 로컬 설치는 애플리케이션의 소스코드들이 확장 모듈과 의존성이 있게 되므로 애플리케이션과 함께 관리합니다. 다시 말해, 로컬 설치는 애플리케이션을 중심으로 해당 애플리케이션이 접근할 수 있는 로컬에 설치되어야 한다는 의미인데, -g 옵션 없이 설치하면 로컬로 설치됩니다. npm list 역시 -g 옵션 없이 사용합니다.

특정 버전의 확장 모듈 설치
특정 버전의 확장 모듈을 설치할 때는 @을 붙이고 버전을 명시합니다.

npm install [모듈명@버전]

npm search [모듈명]
npm info [모듈명]


## 확장모듈 관리
## package.json
package.json
노드로 확장 모듈을 작성하면 npm을 통해 중앙 저장소로 배포할 수 있습니다. package.json 파일은 배포한 모듈 정보를 담고자 만들어졌지만, 노드로 작성하는 애플리케이션도 package.json 파일을 사용하여 관리할 수 있습니다. 꼭 확장 모듈 형태로 배포하기 위한 것이 아니더라도 애플리케이션을 개발할 때 package.json 파일을 이용하면 사용하는 확장 모듈에 대한 의존성 관리가 가능하기 때문에 편리합니다. 

pacakge.json 파일은 기본적으로 CommonJS의 명세를 충실히 따르고 있으며 JSON 형식의 파일입니다.

직접 작성할 수도 있고 npm init 명령을 통해서 자동으로 생성할 수도 있습니다. 그리고 해당 애플리케이션을 위해 사용한 확장 모듈에 대한 정보는 npm install -save를 통해 자동으로 모듈에 대한 정보를 추가할 수 있습니다.

다음은 package.json 파일의 내용과 설명입니다. 기본적으로 프로젝트에 대한 명세라고 할 수 있습니다.


--
Key	Value
name	
프로젝트 이름으로, 가장 중요합니다. 중앙 저장소에 배포할 때 version과 함께 필수 항목입니다.
url로 사용되고, 설치할 때 디렉토리 이름이 되기 때문에 url이나 디렉터리에서 쓸 수 없는 이름을 사용하면 안 됩니다.
또한, 이름에 node나 js가 들어가면 안 됩니다.
name은 214자보다 짧아야 하며, 점(.)이나 밑줄(_)로 시작할 수 없습니다.
대문자를 포함해서는 안 되며, require() 함수의 인수로 사용되며 짧고 알기 쉬운 것으로 짓는 것이 좋습니다.

version	프로젝트 버전을 정의합니다. 3단계 버전을 사용하며, - 로 태그 이름을 적을 수 있습니다.
description	
프로젝트 설명으로, 문자열로 기술합니다.
npm search로 검색된 리스트에 표시되기 때문에 사람들이 패키지를 찾아내고 이해하는 데 도움이 됩니다.

keywords	
프로젝트를 검색할 때 참조되는 키워드입니다.
description과 마찬가지로 npm search로 검색된 리스트에 표시됩니다.

homepage	
프로젝트 홈페이지 주소입니다.
url 항목과는 다르며, url을 설정하면 예상치 못한 움직임을 하게 되므로 주의합니다.

author	프로젝트 작성자 정보로, 한 사람만을 지정합니다. JSON 형식으로 name, email, url 옵션을 포함합니다.
contributors	프로젝트에 참여한 공헌자 정보로, 여러 사람을 배열로 지정할 수 있습니다.
repository	
프로젝트의 소스 코드를 저장한 저장소의 정보입니다.
소스 코드에 참여하고자 하는 사람들에게 도움이 될 수 있습니다. 프로젝트의 홈페이지 url을 명시해서는 안 됩니다.
scripts	프로젝트에서 자주 실행해야 하는 명령어를 scripts로 작성해두면 npm 명령어로 실행 가능합니다.
config	소스 코드에서 config 필드에 있는 값을 환경 변수처럼 사용할 수 있습니다.
private	이 값을 true로 작성하면 중앙 저장소로 저장하지 않습니다.
dependencies	
프로젝트 의존성 관리를 위한 부분입니다. 이 프로젝트가 어떤 확장 모듈을 요구하는지 정리할 수 있습니다.
일반적으로 package.json에서 가장 많은 정보가 입력되는 곳입니다.
애플리케이션을 설치할 때 이 내용을 참조하여 필요한 확장 모듈을 자동으로 설치합니다.
따라서 개발한 애플리케이션이 특정한 확장 모듈을 사용한다면 여기에 꼭 명시를 해주어야 합니다.
또한, npm install 명령은 여기에 포함된 모든 확장 모듈들을 설치하게 되어 있습니다.
devDependencies	개발할 때만 의존하는 확장 모듈을 관리합니다.
engine	실행 가능한 노드 버전의 범위를 결정합니다.

## 확장모듈 - nodemon
nodemon은 node monitor의 약자로, 노드가 실행하는 파일이 속한 디렉터리를 감시하고 있다가 파일이 수정되면 자동으로 노드 애플리케이션을 재시작하는 확장 모듈입니다. 이 확장 모듈을 이용하면 개발 중인 노드 애플리케이션의 소스 코드를 수정할 때마다 매번 노드 명령어를 통해 새로 시작할 필요가 없으므로 매우 편리합니다.


# 04
# 1주차 주요 확장 모듈 - express

## express 설치
## 새 프로젝트
새로운 express 프로젝트를 만드는 것도 Express Generator를 설치하면 아주 간단합니다. 웹 서버를 구동하기 위해 필수적으로 있어야 할 파일들과, 그에 따라서 필요한 폴더 구조들을 자동으로 만들어주는 것이 express-generator입니다. 따라서 express-generator를 이용하면 웹 서버를 쉽게 만들 수 있습니다.

## 내부 구성
app.js 소스 살펴보기
현재 생성된 파일 중에 실행에 큰 영향을 미치는 것이 app.js와 www 입니다. 먼저 app.js에 대해 간단히 살펴보겠습니다.
```js
1
var createError = require('http-errors');
2
var express = require('express');
3
var path = require('path');
4
var cookieParser = require('cookie-parser');
5
var logger = require('morgan');
6
​
7
var indexRouter = require('./routes/index');
8
var usersRouter = require('./routes/users');
9
​
10
var app = express();
11
​
12
// view engine setup
13
app.set('views', path.join(__dirname, 'views'));
14
app.set('view engine', 'jade');
15
​
16
app.use(logger('dev'));
17
app.use(express.json());
18
app.use(express.urlencoded({ extended: false }));
19
app.use(cookieParser());
20
app.use(express.static(path.join(__dirname, 'public')));
21
​
22
​
23
app.use('/', indexRouter);
24
app.use('/users', usersRouter);
25
​
26
// catch 404 and forward to error handler
27
app.use(function(req, res, next) {
28
  next(createError(404));
29
});
30
​
31
// error handler
32
app.use(function(err, req, res, next) {
33
  // set locals, only providing error in development
34
  res.locals.message = err.message;
35
  res.locals.error = req.app.get('env') === 'development' ? err : {};
36
​
37
  // render the error page
38
  res.status(err.status || 500);
39
  res.render('error');
40
});
41
​
42
module.exports = app;
```

js
01~08번 라인

필요한 모듈을 불러오는 단계입니다. 우리가 사용하는 express 외에도 path와 같은 기본 모듈을 불러오는 것을 확인할 수 있습니다. 또한, 우리가 사용하는 페이지들을 라우팅하기 위한 routes와 사용자를 관리하기 위한 user를 각각 하나의 모듈로 불러오는 것을 확인할 수 있습니다.

5번 라인

morgan은 http 리퀘스트에 대해 로깅하는 모듈입니다. 객체를 생성합니다.

10번 라인

app이라는 객체를 선언하고 express() 함수로 생성합니다. 이 객체를 이용하여 웹 서버의 특징을 기술합니다.

12~29번 라인

app 객체에 대한 특징, 즉 우리가 생성할 웹 서버의 특징을 기술하는 부분입니다.

13번 라인

화면을 보이게 할 뷰 템플릿 파일들이 있는 경로를 라우팅하기 위해 그 값을 미리 정의합니다. 화면의 출력을 담당하는 뷰 계층을 구성하는 파일들을 연결하는 부분이라고 이해하면 됩니다. 여기서는 views 폴더로 지정해주었습니다. 따라서 앞으로 뷰 템플릿 파일을 만들고 난 후, views 폴더 안에 넣어주고 라우팅을 설정해주면 됩니다.

14번 라인

뷰에 사용될 기본 엔진의 이름을 정의합니다. express에서는 ejs, pug(구 jade에서 pug로 이름이 변경됨) 등을 지원하고 있습니다.

20번 라인

디렉토리 구조를 URL에 반영하여 쉽게 접근 가능한 정적 디렉토리를 설정합니다.

31~40번 라인

에러 핸들러는 에러가 발생했을 때 어떻게 처리할지에 대한 코드입니다. 에러가 나지 않는 프로그램은 거의 없다고 봐도 될 정도로 에러의 종류는 다양합니다. 따라서 에러 처리가 잘 되어 있는 프로그램이 잘 만들어진 프로그램이라고 말할 수 있을 정도로 에러 처리는 중요한 부분입니다. 기본적으로는 에러가 발생하면 알려주는 메세지 처리를 합니다.

www.js 살펴보기
app.js 소스를 살펴보면 http에 관한 설정이 없습니다. 따라서 이 파일만으로는 웹서버를 구동시킬 수 없습니다. express-generator에서는 http에 관한 설정을 www.js로 따로 빼놓았는데, bin 폴더로 가면 확인할 수 있습니다. 즉, 웹 서버와 관련된 부분은 /bin/www 에 들어있습니다. 앞으로 사용하게 될 npm start라는 명령어도 이 www 파일을 실행시키는 명령어입니다. /bin/www.js 소스에서 포트 설정에 관한 부분만 간단히 살펴봅시다. 


## 페이지 라우팅
express에서 라우팅이라는 개념은 클라이언트로부터 요청받은 URL과 뷰를 매칭시키는 것이라고 할 수 있습니다. 라우팅이라는 사전적인 의미 그대로 특정한 URL에 대해 특정한 뷰로 연결하는 역할입니다. 

URL이라고 했지만 실제로 라우팅에 사용되는 정보는 호스트 이름을 제외하고 나머지 경로를 표시한 문자입니다.

예를 들어 다음과 같은 URL로 접속하면 라우팅 대상은 '/hello'라는 문자열이 됩니다.

http://localhost:3000/hello



app.get 함수는 GET 방식으로 들어오는 경로를 연결하여, 이에 대응하는 동작을 콜백 함수로 기술할 수 있도록 합니다. 지정된 Path '/'으로, 웹 사이트의 루트(root) 페이지로 연결합니다. 루트 페이지란, 제일 처음 보이게 되는 메인 페이지를 의미합니다. 

콜백 함수의 req는 요청객체(Request Object)이고 res는 응답객체(Response Object)입니다. 요청객체에는 클라이언트에서 보낸 여러 정보가 포함되어 있습니다. 응답 객체에는 우리가 클라이언트에 응답할 수 있게 하는 객체인데, 위에서 render() 이라는 함수로 뷰를 렌더링하게 되어 있습니다.

코드를 보면 쉽게 알 수 있듯이, 렌더링할 내용은 index.jade이고 이는 jade 형식으로 표현된 뷰파일입니다. jade는 외부모듈로, 템플릿 엔진 모듈입니다. jade는 후반부 강의에서 자세히 설명하도록 하겠습니다.

즉 한마디로 쉽게 설명하자면, 위 코드는 설정된 경로의 루트 페이지('/')로 접속했을 때, index.jade 페이지를 보여준다는 뜻입니다.

app.post 함수는 POST 방식으로 들어오는 경로를 연결합니다. POST 방식은 express Configuration에서 bodyParser를 포함해서 요청 객체의 body 속성을 통해 클라이언트에서 HTML Form으로 작성한 데이터를 읽어올 수 있습니다.


위 경우 http://localhost:3000/hello/world로 요청을 받았다면 req.params.id에는 'world'라는 문자열이 들어가게 됩니다.

URL을 이용해 값을 넘겨줄 수 있다는 뜻이지요.

만약 methodOverride를 설정에 추가하면 get, post 말고도 put 등의 REST 방식도 사용할 수 있습니다.

(REST 방식이란 Representational State Transfer의 약자로 데이터 전송 방식 중 하나를 의미합니다.)

## 간단한 웹 페이지 이동


# 05
# 2주차 주요 확장 모듈 - express Pug
템플릿 엔진은 동적인 파일과 정적인 파일의 장단점을 결합한 형태의 새로운 체계로, express가 지원하는 템플릿 엔진 중에 가장 유명하고 많이 쓰이는 것이 ejs와 pug입니다.

ejs는 html 태그에 부분적으로 입력 및 수정을 하는 방식으로 html 문법에 익숙한 사람들에게는 적응하기 쉬울 것이고, pug는 코드를 간소화시켜서 컴파일한 후에 html을 렌더링하는 방식이라 생산성이 높지만 문법을 익히는 데 시간이 좀 더 걸릴 수도 있습니다. 어떤 템플릿 엔진을 사용하든 상관이 없으므로 둘 중 취향에 따라 사용하면 됩니다.

pug의 원래 이름은 jade였지만 저작권 문제로 현재 pug로 변경되었습니다. jade로 쓰인 기간이 더 길기 때문에 jade로 더 널리 알려져 있지요. pug 관련 자료를 찾아볼때 jade라고 검색해도 무방합니다.

이 강의에서는 pug를 사용하도록 하겠습니다.  pug는 node.js용으로 만들어진 view 템플릿 엔진으로, pug 문법에 맞게 작성하면 해당 내용을 html이나 자바스크립트로 바꾸어줍니다. 문법이 간단해서 HTML보다 훨씬 사용하기 편리합니다. 

## 표현방법 및 계층구조
## 태그 ID, 클래스, 속성

```pug
html
    head
    body
        div#goormDiv1
        div#goormDiv2.divStyle1
        div.divStyle2
        div.divStyle1.divStyle2
```
```html
<html>
    <head> </head>
    <body>
        <div id="goormDiv1"></div>
        <div id="goormDiv2" class="divStyle1"></div>
        <div class="divStyle2"></div> 
        <div class="divStyle1 divStyle2"></div>
    </body>
</html>
```
div 태그는 생략가능.

```pug
#contents(style="border:1px solid black;")
    input(type="checkbox", checked)
```
```html
<div id="contents" style="border:1px solid black;">
    <input type="checkbox" checked />
</div> 
```

## 태그 콘텐츠
```pug
html
    head
    body
        div#goormElement1
            | edu.goorm.io
            | 구름EDU 사이트
```
```html
<html>
    <head> </head>
    <body>
        <div id="goormElement1">edu.goorm.io 구름EDU 사이트</div>
    </body>
</html>
```
#{fieldname} 으로 동적 데이터 받아오기 가능
```pug
html
    head
        title= title
    body
        div#subject #{title}
        div#msg #{message}
```
만약 html 태그 포함했다면, !{}로 출력해야 제대로 보임.

## 자바스크립트와 CSS
pug는 script와 style 태그에 한해서 | 세로선을 사용 안해도 여러 줄로 표현 가능하다.

주석 : //
실제 출력 시 주석 생략하기 (언버퍼드 코멘트 - unbuffered comment) : //-


## 설치 및 예제
## Pug를 이용한 웹페이지 실습

pug는 for문 사용 가능.
```pug
// index.pug

html
	head
		title= title
	body
		h1 Hello #{title}!
		ul
			-for(var i=0; i<5; i++)
				li 순서없는목록 #{i + 1}
		ol
			-for(var i=0; i<5; i++)
				li 순서있는목록 #{i + 1}
```

```js
// app.js
..
// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');
```

# 06
# 2주차 주요 확장 모듈 - socket.io
## 클라이언트/서버 통신
통신 프로토콜
통신 서비스 또는 기능 수행을 위해 관련 통신 당사자 간 교환하는 정보의 종류와 표현 형식, 교환 절차, 그리고 교환 과정에서 실행해야 할 행위에 관한 규약입니다.

대표적인 통신 프로토콜로는 IBM의 폐쇄형 망 구조인 SNA와 개방형 망 구조인 TCP/IP가 있습니다. TCP/IP 응용 계층에 적용 확장된 프로토콜로는 전자 우편 서비스를 위한 SMTP, 파일 전송 서비스를 위한 FTP, 망 관리 서비스를 위한 SNMP, 그리고 우리가 주로 다루게 될 웹 서비스를 위한 HTTP 등이 있습니다.

일반적으로 서버 프로세스는 클라이언트보다 먼저 실행되어 대기 상태에 있으므로 클라이언트의 연결 요청에 항상 응답할 준비가 되어 있습니다. 서버 프로세스는 일단 시작하면 영원히 종료되지 않고 실행되며, 다수의 클라이언트 요청을 반복적으로 수행합니다. 클라이언트와 서버 사이의 네트워크 연결은 전송 계층의 포트 연결로 구현됩니다.


Polling 방식은 클라이언트가 서버에 주기적으로 요청 후 응답을 받는 방식입니다. 가장 기본적인 기법으로 구현이 간단하지만 쓸모없는 요청과 응답 때문에 많은 트래픽이 낭비되며, 다음 폴링이 이루어지기 전까지 어떤 이벤트가 왔는지 모르기 때문에 실시간성이 보장되지 않습니다. 요청 주기를 조절할 수 있기 때문에 짧게 줄일 수도 있지만, 요청 주기가 짧으면 서버에 부하를 줄 수 있으므로 주의해야 합니다. 실시간 메시지 전달이 크게 중요하지 않은 서비스에 적합한 방식입니다.
![](https://grm-project-template-bucket.s3.ap-northeast-2.amazonaws.com/lesson/les_JzfYj_1658467753820/0f66b63f93bd90547578c966fad29fc6ce45ce606da98fa253e2f476578b79a7.gif)



Long Poll 방식은 Polling 방식의 단점인 반복적인 요청으로 응답을 받는 형태에서, Client가 서버에 대한 요청을 유지하여 반복적인 요청을 없애고 유효한 이벤트가 발생하면 응답을 해주는 방식입니다. 즉 Long이라는 이름과 같이 오래 접속을 유지하는 것인데, 응답을 기다리다가 응답이 오면 데이터를 처리함과 동시에 새로운 접속을 생성하는 것입니다. 단, 무한정 기다리는 것이 아니라 일정 시간이 지나면 접속을 완료하고 새로 요청합니다. Polling 방식에 비해 불필요한 요청과 응답을 줄일 수 있습니다. 
![](https://grm-project-template-bucket.s3.ap-northeast-2.amazonaws.com/lesson/les_JzfYj_1658467753820/e82aafdef81648cd649201f89c5c0473c99b0afe34bf898e757b8f2209cd9a86.gif)



WebSocket 방식은 이러한 불편점들을 개선하기 위해 만들어진 HTML5 표준 기술로, Client와 서버가 연결된 후부터 HTTP 요청/응답과는 상관없이 서버와 양방향 통신이 가능합니다. 웹 소켓에 대한 좀 더 자세한 내용은 바로 다음 강의에서 다루도록 하겠습니다.
![](https://grm-project-template-bucket.s3.ap-northeast-2.amazonaws.com/lesson/les_JzfYj_1658467753820/ba599efc70385d775a613cc9c8f1dbec8be63fee0219e8f50c5538cd45e73906.gif)




## Web Socket이란?
웹소켓은 HTML5 표준 기술로, 사용자의 브라우저와 서버 사이의 동적인 양방향 연결 채널을 구성합니다. Websocket API를 통해 서버로 메세지를 보내고, 요청 없이 응답을 받아오는 것이 가능합니다. 현재 API는 W3C에서 관장하고 있으며 프로토콜은 IETF에서 관리하고 있습니다. 웹소켓은 별도의 포트를 사용하지 않고 HTTP와 같은 80번 포트를 사용하고 있는데, 이 때문에 클라이언트인 웹 브라우저뿐만 아니라 웹 서버도 기능을 지원하고 있어야만 합니다. 


Socket.io
그러나 웹소켓은 HTML5의 기술이기 때문에 오래된 버전의 웹 브라우저는 웹소켓을 지원하지 않습니다. 특히 자동 업데이트가 되지 않는 익스플로러 구 버전 사용자들은 웹소켓으로 작성된 웹페이지를 볼 수 없지요. 따라서 이를 해결하기 위해 나온 여러 기술 중 하나가 Socket.io입니다. 웹페이지가 열리는 브라우저가 웹소켓을 지원하면 웹소켓 방식으로 동작하고, 지원하지 않는 브라우저라면 일반 http를 이용해서 실시간 통신을 흉내내는 것입니다.

Socket.io는 node.js 기반으로 만들어진 기술로, 거의 모든 웹 브라우저와 모바일 장치를 지원하는 실시간 웹 애플리케이션 지원 라이브러리입니다. 이것은 100% 자바스크립트로 구현되어 있으며, 현존하는 대부분의 실시간 웹 기술들을 추상화해 놓았습니다. 다시 말해, Socket.io는 자바스크립트를 이용하여 브라우저 종류에 상관없이 실시간 웹을 구현할 수 있도록 한 기술입니다.

Socket.io는 웹 브라우저와 웹 서버의 종류와 버전을 파악하여 가장 적합한 기술을 선택하여 사용합니다. 만약 브라우저에 FlashSocket이라는 기술을 지원하는 플러그인이 설치되어 있으면 그것을 사용하고 플러그인이 없으면 AJAX Long Polling 방식을 사용하도록 합니다.



왜 웹소켓을 사용하는가?
초창기 웹은 단순히 인터넷에 접속한 사용자에게 콘텐츠를 전달하는 역할에 지나지 않았습니다. 사용자와의 상호작용은 크게 중요하지 않았으며, 정보의 검색 및 열람 수준에 그쳤습니다. 하지만 웹을 통해 사용자들이 정보를 교환하고 스스로 커뮤니티를 만들어 교류하고자 하는 수요가 늘어나면서 게시판, 블로그 등과 같은 서버와 클라이언트 간의 상호작용을 하는 부분들이 생기기 시작했습니다. 인터넷과 웹이 태동했던 CERN과 같은 초창기의 연구기관에서 사용하던 것과 달리 오늘날의 웹은 일상생활 깊숙이 파고들었고, 네이티브 애플리케이션을 대체하는 수준에 이르렀습니다. 특히 전형적인 브라우저 렌더링 방식은 HTTP 요청에 대한 HTTP 응답을 받아서 브라우저의 화면을 모두 지우고 받은 내용을 새로 표시하는 방식이었습니다. 그때 Ajax와 같은 기술이 나타나면서 사용자와 긴밀히 상호작용하는 웹 서비스가 등장하였고 인기를 끌기 시작하였습니다. 이러한 RIA(Rich Internet Application) 기술의 발달이 웹소켓의 등장 배경이라고 할 수 있습니다.

다시 말해, 기존에는 서버와 클라이언트가 실시간으로 상호작용하는 웹 서비스를 개발하기 위해서 숨겨진 프레임을 이용하는 방법이나 Long Polling, Stream 등과 같은 다양한 방법을 사용했었습니다. 하지만 이 방식은 브라우저가 HTTP 요청을 보내고 웹 서버가 이 요청에 대한 HTTP 응답을 보내는 단방향의 메시지 교환 방식을 유지하는 선에서 구현된 방식입니다. 즉, 기존의 방법에 일종의 트릭을 사용한 방법입니다. 이 때문에 기존의 웹 기술을 이용하여 실시간 웹 서비스를 만드는 일은 복잡하고 어려웠습니다.

바로 이러한 불편함과 사용자와 긴밀히 상호작용하는 웹 페이지를 더 쉽게 만들고자 하는 개발자의 요구가 브라우저와 웹 서버 사이의 자유로운 양방향 메시지 송수신 방법으로써 HTML5 표준안의 일부인 웹소켓 API가 등장했습니다. 

사용 방법은 Ajax와 비슷하지만, 개념 면에서 Ajax와 차이를 두고 있습니다. Ajax의 경우는 웹 브라우저에서 데이터를 호출하면 웹 서버에서 호출된 값을 검색, 작성해서 웹 브라우저로 메세지를 보내는 형식의 구조라면 웹소켓의 경우는 웹 브라우저에서 호출해서 데이터를 가져가는 기능을 포함하여 반대로 서버에서 클라이언트를 호출할 수 있는 기능까지 있습니다.

예로 채팅프로그램을 만든다고 가정할 때, 우리가 채팅을 서버로 보내는 건 가능합니다. 그러나 Ajax로 만든 웹 페이지라면 서버 측에서 클라이언트가 보낼 수가 없습니다. 대응책으로 10초마다 데이터를 갱신해서 확인할 수 있지만, 웹소켓은 서버에서도 클라이언트를 인지하는 상태이기에 양방향 통신이 가능합니다.

HTML5 웹소켓은 매우 유용한 기술이지만, 브라우저별로 지원하는 웹소켓 버전이 다르며 오래된 브라우저의 경우 아예 지원하지 않습니다. 따라서 자바스크립트를 이용하여 브라우저에 상관없이 실시간 웹을 구현할 수 있는 Socket.io를 좀 더 많이 사용하고 있습니다.


Socket.io 설치
Socket.io도 웹소켓과 마찬가지로 브라우저에서 자바스크립트를 사용합니다. 웹소켓 프로토콜 자체는 IETF가 관장하는 표준 프로토콜이므로 여러 서버가 지원하고 있지만 Socket.io는 Node.js의 모듈로 지원하고 있습니다.

이전 장에서 다룬 npm install 명령어로 간단히 설치할 수 있습니다.


## 이벤트 주고 받기
Socket.io는 비동기 통신을 위한 라이브러리이므로 이벤트 기반의 처리에 의존하고 있습니다. 간단한 예제로 이벤트를 주고받아 보고, 코드를 보면서 socket을 어떻게 사용하는지 알아보겠습니다. 아래 코드를 작성해 봅시다.

```js
//server.js

var app = require('http').createServer(handler),
    io = require('socket.io').listen(app),
    fs = require('fs');

app.listen(3000);

function handler (req, res) {
	fs.readFile('index.html', function (err, data) {
		if (err) {
			res.writeHead(500);
			return res.end('Error loading index.html');
		}
		res.writeHead(200);
		res.end(data);
	});
}

io.on('connection', function (socket) {  // 1
	socket.emit('news', { serverData : "서버 작동" });
	
	socket.on('client login', function (data) {  // 2
		console.log(data);
	});
		
	socket.on('disconnect', function(){  // 3
		console.log('접속이 종료되었습니다.');
	});

});
```

socket.io를 사용한 간단한 기본 코드입니다.

20번째 줄의 주석 1번 전까지의 코드는 접속했을 때 index.html 페이지를 불러오고, 에러가 났을 때 처리해주는 코드입니다.
20번째 줄에서 보이는 connection은 socket.io의 기본 이벤트로, 사용자가 웹사이트를 열면 자동으로 발생하는 이벤트입니다. 이때 이벤트 안의 함수에는 접속한 사용자의 socket이 파라미터로 전달되는데, 접속한 각 클라이언트에 관련한 이벤트들을 작성하려면 이 connection 리스너 함수 안에서 socket을 사용하면 됩니다.
connection 안에 각 이벤트를 작성할 때는 socket.on('EVENT 이름', 함수) 형식으로 작성하면 됩니다. 함수 대신 전달하고 싶은 값이 있다면, 변수를 넣어주어도 됩니다.
socket.emit은 event를 발생시키는 함수입니다. 이렇게 서버쪽에서 이벤트를 발생시키면 클라이언트 페이지의 해당 이벤트 리스너에서 처리되게 됩니다. 위 코드에서는 emit을 이용해 "news" 이벤트를 발생시켜 주었습니다. socket.emit을 이용하면 해당 socket을 통해 상대편으로 전달하고, io.emit을 이용하면 서버가 현재 접속해있는 모든 클라이언트에게 이벤트를 전달합니다. 이 코드에서는 사용자가 맨 처음으로 접속했을 때 news 이벤트가 발생하게 되며, serverData라는 변수에 문자열을 넣어서 전달해 주었습니다.
23번째 줄 주석 2번에서는 client login라는 이벤트를 만들어서, 콘솔 창에 전달받은 data를 찍어주었습니다.
27번째 줄 주석 3번에서 보이는 disconnect도 connection처럼 socket.io의 기본이벤트인데, 사용자의 접속이 끊어지면 자동으로 발생합니다. 단, disconnect 이벤트는 개별 클라이언트가 접속이 끊어졌을 때 발생하는 이벤트이므로 io.on이 아닌 socket.on으로 작성해줘야 한다는 점 주의하세요.

```js
<!-- index.html -->

<script src="/socket.io/socket.io.js"></script>
<script>
var socket = io.connect('http://localhost:3000');
//구름ide 이용자는 localhost가 아닌 자신의 url을 입력. ex) http://test-1.run.goorm.io/ 

socket.on('news', function (data) {
	console.log(data);
	socket.emit('client login', { clientData : '클라이언트 접속' });
});
	   
</script>
```
클라이언트 페이지인 index.html입니다.

이 코드의 이벤트 처리는 딱 하나밖에 없는데, 바로 news 이벤트입니다. news 이벤트가 발생하면 클라이언트 페이지에서는 콘솔 창에 전달받은 data를 출력해줍니다. 여기서 주의해야 할 점은, 서버의 콘솔 창에 찍히는 것이 아니라 클라이언트 페이지의 콘솔 창에 찍힌다는 것이지요. 따라서 웹 페이지의 개발자 도구를 클릭하면 출력된 값을 볼 수 있습니다. 크롬의 경우는 아래와 같이 도구 더보기를 이용해 보면 되고, 익스플로러의 경우에는 F12번을 누르시면 볼 수 있습니다.

그 후 client login 이벤트를 발생시키면서, clientData라는 변수에 문자열을 넣어 전달해줍니다. 따라서 이 clientData가 server.js의 client login 이벤트로 전달된 후, 콘솔 창에 찍히게 됩니다.

이제 코드를 다 작성했으면 node server.js로 서버를 실행시켜줍니다.

전 강좌에서 socket.io를 만약 글로벌로 전역 설치했다면 아래와 같은 오류가 뜰 수도 있는데, 그럴 땐 npm link socket.io 명령어를 실행해서 링크를 잡아주거나 로컬로 설치하면 됩니다.

***
TypeError: require(...).listen is not a function 오류

socket이 3.0으로 업데이트 되어 문법이 달라졌다고 함.
https://codingapple.com/forums/topic/socket-io-%EA%B4%80%EB%A0%A8/

왜 안되지... => express 프로젝트 내에 파일을 넣고 실행해야 하는가??





## socket.io를 이용한 채팅 구현 - 구현에 앞서
socket.io를 이용한 채팅 구현 - 구현에 앞서
socket.io에 대해 간단하게 배워보았으니, 이제 socket.io를 사용하는 기본 예제라 할 수 있는 채팅 프로그램을 만들어보겠습니다. 실제 채팅 페이지를 만들어 봅시다.

주요 기능
이번 챕터에서 구현할 채팅 페이지에는 아래와 같은 주요 기능이 있습니다.

접속하면 알림 출력
닉네임 변경 가능
닉네임 변경했을 때 알림 출력
유저가 떠났을 경우 알림 출력

## socket.io를 이용한 채팅 구현 - 기본

express-generator를 이용해 새 프로젝트를 새로 생성해준 후, 이동해서 npm install 까지 완료해주세요. 프로젝트 폴더 이름은 아무거나 하셔도 좋습니다. 저는 socket-test로 하겠습니다.

어떻게 하는지 기억이 잘 나지 않으신다면, 8장 express 챕터의 "새 프로젝트"라는 강의를 참고해주세요.

그 후 채팅을 만드는 데 필요한 socket.io, Pug를 설치해주세요. 

이제 본격적으로 채팅 페이지를 만들어 보도록 하겠습니다. 기본적으로 같은 페이지에 접속한 사람들과의 채팅이 가능해야겠지요?

추가 기능으로, 닉네임 변경을 하거나 새로운 사람이 접속했을 때, 접속을 끊을 때도 채팅창에 알림 문구가 뜨도록 만들어봅시다. 이번 기본 강의에서는 채팅을 주고받는 기본 기능까지만 진행하겠습니다.

Pug와 소켓을 배웠기 때문에, 일반 HTML이 아닌 Pug를 이용해서 만들어보도록 하겠습니다. 또, 채팅창의 모양을 결정하는 스타일 부분도 CSS로 따로 빼낼 예정입니다.

기본 HTML만 사용하면 투박한 느낌이 드니까 깔끔한 디자인을 위해 부트스트랩도 적용했습니다. 컴포넌트가 많은 건 아니라 디자인에 큰 차이가 나는 것은 아니지만요.

위의 화면이 부트스트랩을 적용한 화면입니다. 부트스트랩은 프론트엔드 프레임워크로, 웹사이트를 만들 때 좀 더 쉽게 꾸밀 수 있도록 도와줍니다.

먼저, 서버를 작동시키는 server.js를 생성해봅시다. express-generator로 생성했을 경우 서버 코드는 www로 분리되어 있지만 이번 채팅 예제에서는 따로 www로 빼지 않고 server.js 코드 하나에 서버 코드를 모두 작성하도록 하겠습니다. 따라서 이번 강의에서는 지금까지 했던 것처럼 npm start로 서버를 구동시키는 것이 아니라, node server로 서버를 구동시킵니다.

```js
// server.js

var express = require('express');
var app = express();
var http = require('http').Server(app); 
var io = require('socket.io')(http);    
var path = require('path');

app.set('views', './views');
app.set('view engine', 'pug');
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
	// 루트 페이지로 접속시 chat.pug 렌더링
	res.render('chat');
});

var count=1; 
// 채팅방에 접속했을 때 - 1
io.on('connection', function(socket){
	console.log('user connected: ', socket.id);
	var name = "익명" + count++;
	socket.name = name;
	io.to(socket.id).emit('create name', name);
	
	// 채팅방 접속이 끊어졌을 때 - 2
	socket.on('disconnect', function(){
		console.log('user disconnected: '+ socket.id + ' ' + socket.name);
	});
	
	// 메세지를 보냈을 때 - 3 
	socket.on('send message', function(name, text){
		var msg = name + ' : ' + text;
		socket.name = name;
		console.log(msg);
		io.emit('receive message', msg);
	});
	
});

http.listen(3000, function(){ 
	console.log('server on..');
});
```
1번 - 채팅방에 접속했을 때

사용자가 채팅 페이지에 접속하면 사용자를 구별하는 socket.id를 "user connected"라는 말과 함께 서버 콘솔에 찍어줍니다. 이 id는 자동 생성되는 영어와 숫자를 사용하는 문자열로, 채팅방에서 사용할 닉네임과는 다릅니다.
처음 접속했을 때에는 익명1, 익명2와 같은 순서로 닉네임이 생성됩니다. 따라서 이 변수 name에 값을 넣어줍니다.
또 닉네임이 변경될 때 비교해주기 위한 값이 필요하기 때문에, socket.name에도 현재 생성된 닉네임 값을 넣어줍니다.
이 부분은 전 강의에서 다뤄지지 않았던 내용인데, io.to(socket.id).emit은 서버가 해당 socket id에만 이벤트를 전달합니다. 채팅방에 접속한 유저마다 닉네임이 다른데, 모두 바뀌지 않고 각 유저에게만 닉네임이 보여지기 위해 io.to(socket.id).emit을 이용해서 create name이라는 이벤트를 발생시켜줍니다.
2번 - 채팅방 접속이 끊어졌을 때

접속한 사용자가 채팅방을 나가면, "user disconnected"라는 말과 함께 socket.id와 socket.name을 서버 콘솔에 찍어줍니다.
3번 - 메세지를 보냈을 때

사용자가 전송 버튼을 눌러서 메세지를 보냈을 경우, 채팅방에 출력해줄 메세지를 msg 변수에 넣어줍니다. 여기서는 닉네임과 메세지를 합쳐줍니다.
사용자가 닉네임을 변경했을 때를 위해 socket.name에 전달받은 name을 넣어줍니다. 
서버 콘솔에 메세지를 출력해 주고, receive message 라는 이벤트를 발생시키고 메세지를 전달해 줍니다.
이제 채팅창의 화면과 버튼을 넣고, 클라이언트쪽 처리를 해주는 chat.pug를 생성해봅시다. views 폴더에 생성하면 됩니다.


```pug
// chat.pug

doctype 5
html
  head
    title= 'Chat'
    link(rel='stylesheet', href='/stylesheets/style.css')
    link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css", integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous")
    // 위 link와 이 script는 부트스트랩 연결
    script(src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js", integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous")  
    script(src='/socket.io/socket.io.js')
    script(src='//code.jquery.com/jquery-1.11.1.js')
  body
    center
      div
        // 부트스트랩 버튼
        button.btn.btn-info(type='button') Goorm 채팅방  
      div
        // 부트스트랩 textarea
        textarea#chatLog.form-control(readonly='')  
      form#chat
        // 부트스트랩 input
        input#name.form-control(type='text')
        // 부트스트랩 input
        input#message.form-control(type='text')
        // 부트스트랩 버튼
        button.btn.btn-primary(type='submit') 전송
      #box.box

    script.
      var socket = io(); 

      // 전송 버튼을 누를 때 - 1
      $('#chat').on('submit', function(e){   
      socket.emit('send message', $('#name').val(), $('#message').val());
      $('#message').val('');
      $('#message').focus();
      e.preventDefault();
      });
			
      // 이름 셋팅 - 2
      socket.on('create name', function(name){
      $('#name').val(name);
      });

      // 메세지를 받았을 때 - 3
      socket.on('receive message', function(msg){
      $('#chatLog').append(msg+'\n');
      $('#chatLog').scrollTop($('#chatLog')[0].scrollHeight);
      });
```
1번 - 전송 버튼을 누를 때

채팅 페이지에서 전송버튼을 눌렀을 때, send message 이벤트를 발생해주면서 name input에 있는 값과 message input에 있는 값을 전달시켜줍니다.
message input에 들어있는 값을 초기화시켜 줍니다.
2번 - 이름 세팅

name input에 전달받은 name 값을 넣어줍니다.
3번 - 메세지를 받았을 때

채팅창 화면에 전달받은 메세지를 출력시켜줍니다.
채팅창에 스크롤이 생기면 제일 아래쪽으로 스크롤을 내려줍니다.
이렇게 생성하면 기본적으로 이름과 메세지 입력 칸, 전송버튼, 메세지를 볼 수 있는 textarea 부분이 생성됩니다.

하지만 CSS를 설정하지 않으니 칸이 작아서 너무 보기 불편합니다. 이제 채팅창 부분을 좀 더 키우고, 버튼에 색깔도 넣어 보겠습니다.

link(rel='stylesheet', href='/stylesheets/style.css')

를 통해 style.css를 연결해주었으니 public/stylesheets 폴더에 style.css 파일을 생성해줍시다.


## socket.io를 이용한 채팅 구현 - 추가 기능
알림 문구는 어떤 사용자가 어떤 닉네임으로 변경했는지만 알려준다면, 원하는 대로 쓰셔도 됩니다. 저는 좀 더 눈에 잘 보이도록 "<알림>"이라는 문구를 맨 앞에 넣어주었습니다.

이제 추가할 코드를 살펴보도록 하겠습니다.
```js
// server.js

var express = require('express');
var app = express();
var http = require('http').Server(app); 
var io = require('socket.io')(http);    
var path = require('path');

app.set('views', './views');
app.set('view engine', 'pug');
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {  
  res.render('chat');
});

var count=1;
io.on('connection', function(socket){   // 채팅방에 접속했을 때 - 1
  	console.log('user connected: ', socket.id);  
  	var name = "익명" + count++;                 
	socket.name = name;
  	io.to(socket.id).emit('create name', name);   
	io.emit('new_connect', name);
	
	socket.on('disconnect', function(){   // 채팅방 접속이 끊어졌을 때 - 2
	  console.log('user disconnected: '+ socket.id + ' ' + socket.name);
	  io.emit('new_disconnect', socket.name);
	});

	socket.on('send message', function(name, text){   // 메세지를 보냈을 때 - 3
		var msg = name + ' : ' + text;
		if(name != socket.name)   // 닉네임을 바꿨을 때 
			io.emit('change name', socket.name, name);
		socket.name = name;
    	console.log(msg);
    	io.emit('receive message', msg);
	});
	
});

http.listen(3000, function(){ 
	console.log('server on..');
});
```
1번 - 채팅방에 접속했을 때

기본 기능에서 달라진 코드는 한 줄 밖에 없습니다. 바로 new_connect 이벤트를 생성하는 io.emit 이죠. 모든 사용자에게 접속 알림을 주어야 하기 때문에, socket.emit이 아닌 io.emit을 사용하였습니다. 어떤 사용자가 접속했는지 알려주어야 하므로, 처음으로 생성된 닉네임값인 name을 전달해주었습니다. socket.name에도 name이 들어가 있기 때문에 socket.name을 전달해도 상관없습니다.
2번 - 채팅방 접속이 끊어졌을 때

여기서도 마찬가지로 딱 한 줄만 추가되었습니다. new_disconnect 이벤트를 생성하는 io.emit입니다. 퇴장 알림도 모든 사용자에게 알려주어야 하므로 io를 사용했고, 퇴장한 사용자의 이름이 저장되어 있는 socket.name을 전달해주었습니다.
3번 - 메세지를 보냈을 때

여기서는 두 줄이 추가되었는데, 바로 닉네임을 바꿨을 때의 조건문입니다. 클라이언트 페이지에서 닉네임값은 name으로 들어오는데, 아직 socket.name은 바뀌기 전이므로 이 두 값을 비교하면 닉네임이 바뀌었는지 알 수 있습니다. 만약 닉네임이 바뀌었으면, change name이라는 이벤트를 발생시킵니다. 그리고 알림을 줄 때 바뀌기 전 닉네임과 새로운 닉네임 값이 필요하므로 둘 다 전달해줍니다.

```pug
// chat.pug

doctype 5
html
  head
    title= 'Chat'
    link(rel='stylesheet', href='/stylesheets/style.css')
    link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css", integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous")
    script(src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js", integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous")
    script(src='/socket.io/socket.io.js')
    script(src='//code.jquery.com/jquery-1.11.1.js')
  body
    center
      div
        button.btn.btn-info(type='button') Goorm 채팅방
      div
        textarea#chatLog.form-control(readonly='')
      form#chat
        input#name.form-control(type='text')
        input#message.form-control(type='text')
        button.btn.btn-primary(type='submit') 전송
      #box.box
	  
    script.
      var socket = io(); 
	  
      $('#chat').on('submit', function(e){   // 전송 버튼을 누를 때 - 1
      socket.emit('send message', $('#name').val(), $('#message').val());
      $('#message').val('');
      $('#message').focus();
      e.preventDefault();
      });
	  
      socket.on('create name', function(name){   // 이름 셋팅 - 2
      $('#name').val(name);
      });
	  
      socket.on('change name', function(oldname, name){   // 닉네임을 바꿨을 때 - 3
      $('#chatLog').append('<알림> ' + oldname + '님이 ' + name +'님으로 닉네임을 변경했습니다.\n');
      });
	  
      socket.on('receive message', function(msg){   // 메세지를 받았을 때 - 4
      $('#chatLog').append(msg+'\n');
      $('#chatLog').scrollTop($('#chatLog')[0].scrollHeight);
      });
	  
      socket.on('new_disconnect', function(name){  // 채팅방 접속이 끊어졌을 때 - 5
      $('#chatLog').append('<알림> ' + name + '님이 채팅창을 떠났습니다.\n');
      });
	  
      socket.on('new_connect', function(name){  // 채팅방에 접속했을 때 - 6
      $('#chatLog').append('<알림> ' + name + '님이 채팅창에 접속했습니다.\n');
      });
```
3번 - 닉네임을 바꿨을 때

1번과 2번은 기본 강의와 동일하므로 생략합니다. 2번과 마찬가지로 닉네임을 바꿨을 때도 닉네임 input의 값을 바꿔줍니다. 그리고 전달받은 전 닉네임과 새로운 닉네임을 이용하여 chatLog에 출력해줍니다. 알림 문구는 원하는 대로 쓰시면 됩니다.
5번 - 채팅방 접속이 끊어졌을 때

새로 생긴 이벤트 리스너입니다. 닉네임을 바꿨을 때와 비슷하게 전달받은 이름을 이용하여 채팅창을 떠났다는 알림을 출력해줍니다.
6번 - 채팅방에 접속했을 때

5번과 동일합니다. 새로운 사용자가 접속했다는 알림을 출력해줍니다.

닉네임을 변경했을 때, 새로운 사용자가 들어왔을때, 사용자가 채팅방을 나갔을 때 알림이 뜨도록 기능을 추가해봅시다.

## socket.io를 이용한 채팅 구현 - 도전 문제
채팅 페이지가 완성되었습니다.

추가 기능 강의를 이용해 알림 기능도 넣어보았는데, 그 외에도 채팅 페이지에 다양한 기능을 추가하는데 도전해보세요.

UI 더 예쁘게 꾸며보기
실시간으로 접속중인 유저 이름 보여주기
그 외 추가해보고 싶은 기능