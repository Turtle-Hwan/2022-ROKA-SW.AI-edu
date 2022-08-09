# HTML + CSS 강의

## vscode 확장 추천  
01. Material Theme : 테마 변경  
02. Material Icon Theme : 아이콘 변경  
03. Auto Rename Tag : html 태그 한 쪽만 변경해도 자동 변경  
04. HTML to CSS autocompletion : 사용 중인 html 태그를 css 파일에서 자동 완성 불러오기 지원  
05. HTML CSS Support : css 파일에서 새로 정의한 클래스 등을 html 문서에서 자동완성 지원  
06. CSS peek : css 태그 위치 바로 찾기  
07. Autoprefixer : css3의 벤더 프리픽스(구버전 브라우저 지원) 한 번에 적용    
08. Bracket Pair Colorizer 2 : 동일 괄호 색깔로 구분  
09. indent-rainbow : 들여쓰기 색깔로 구분  
10. Live Server : 작성 중인 코드 브라우저에서 새로고침 안하고 바로 확인 가능



## seo에 h 태그 중요

하나의 문서에 h1 태그 하나 사용.  
중요한 내용만 담기.  
h1부터 순차적으로 사용해야 한다는 규칙을 지켜야 seo(검색엔진최적화)에 잘 반영된다.



## p,br

p는 브라우저 한 줄이다.  
공백을 많이 주려면 &nbsp 등의 엔티티 필요하다.

br로 줄바꿈 가능하다.
긴 내용을 쓸 때는 하나의 p태그로 단락표현하되 줄바꿈시 br사용하면 좋다.



## a 내부링크 외부링크

내부링크: 문서 내부의 특정 태그 id를 #과 함께 입력해두면 여기로 이동한다.  
목차에 많이 사용한다.
```html
<a href="#one">one으로 이동</a>

<p id="one">this is one</p>
```

외부링크: href="해당 사이트 url"을 입력하면 해당 사이트로 이동한다.  

- target="_blank" : target 속성에 블랭크 값을 주면 새탭에서 링크열기가 된다.




## img 태그
`<img>` : 닫는 태그 없는 빈 태그
```html
<img src="경로" alt="이미지 설명하는 대체 text">

- alt 속성은 이미지가 깨졌을 때도 출력된다.
- src 경로에 외부링크를 넣으면 외부 리소스 참조 가능
```
```html
<a href="#one">one으로 이동
    <img src="경로" alt="이미지 설명하는 대체 text">
</a>
이미지 누를 시 페이지 이동
```

./ : 현재 폴더 경로  
../ : 상위 폴더 경로  
../../ : 상위 폴더의 상위 폴더  


## 상황에 맞는 적절한 태그 사용
어떤 태그를 쓰더라도 css 잘 쓰면 원하는 모양 만들 수 있음. 그러나 html 태그는 그 안의 내용을 의미하는 것이기 때문에 상황에 맞지 않는 태그를 쓰면 검색엔진 등에서 내용 파악이 힘들어진다.


## 텍스트 강조
`<strong></strong>` : 중요한(important) 텍스트 나타낼 때 사용한다.  
출력 시 굵게 나타난다.  
중요한 : 사용자에게 반드시 전달되어야 할 것.

`<em></em>` : 강조(emphasis) 텍스트 나타낼 때 사용한다.  
출력 시 기울여 나타난다.  
강조 : 글 중에서 어조, 볼륨 변화가 필요한 곳.

strong, strong, em, em 두 번 중첩, 혼용 중첩 가능하며, 더욱 강조하는 의미이다.  

`<b></b>` : 출력 시 굵게 나타난다.  
html 구문적으로 중요함의 의미가 없으며, 단순히 시각적으로 굵게 표시할 뿐이다.

`<i></i>` : 출력 시 기울여 나타난다.   
html 구문적으로 강조의 의미가 없으며, 단순히 시각적으로 기울여 표시할 뿐이다.



## 목록 태그
`<ul></ul>` : unordered list / 비순서형 목록 태그  
하위에 `<li></li>` list item 요소들을 포함시켜서 사용한다.  
기본적으로 들여쓰기 및 특수기호가 추가된다.

`<ol></ol>` : ordered list / 순서형 목록 태그  
하위에 `<li></li>` list item 요소들을 포함시켜서 사용한다.    
기본적으로 들여쓰기 및 순서 기호가 추가되며, `<ol type="1">` 타입 지정으로 기호 모양 지정 가능하다.

`<dl></dl>` :  definition list / 정의형 목록 태그  
하위에 `<dt></dt>` definition title, `<dd></dd>` difiniton data 태크를 가질 수 있고, 용어의 정의와 설명을 각각 풀어쓰는 태그이다. 
  




## CSS 실행 법
1. 내부 스타일 시트  
html 문서 내 `<head>` 안에 `<style></style>` 사이에 css 입력하는 방식

2. 외부 스타일 시트  
html 문서 내 `<head>` 안에 `<link href="" rel="stylesheet">`로 외부 파일 불러오기

3. 인라인 스타일 시트  
html 태그 내에 style="" 속성 사용


## CSS 기본 문법 : 선택자{속성:속성값;}
중괄호 부분 : 선언부라 부른다.  
selector, 선택자는 스타일링 하고 싶은 html 태그를 선택한다.  
declaratives, 선언부는 스타일링 하고 싶은 속성과 값을 작성하는 영역이다.


## CSS color속성과 색상 단위 unit
```css
h1{
    color: red;
}
```
<색상 표현 방법>  
키워드 방법 : red, blue 등의 색상 이름을 적는 것.  
RGB 방법 : `rgb(R, G, B)`, 각 RGB에 0~255 사이의 숫자를 넣어 해당 색을 표현. `rgba(R, G, B, T)`에서 T값은 투명도.  
HEX 방법 : `#RRGGBB`에 각 RGB에 해당하는 자리에 0~f를 넣어서 16진수로 표현하는 방법


## CSS font-size 속성과 크기 단위(units)
font-size : 폰트 크기 변경 (text, 글자)

<크기 단위>  
px(pixel) : 고정적인 해상도에 따른 크기  
rem(root em) : root는 최상의 html 태그, em은 배수를 의미한다. `<html>`태그에 적용된 폰트(기본이 16px)의 배수로 적용하고 싶을 때 사용한다.  
em : 부모 태그의 폰트 크기의 배수로 적용된다.  
vw(viewport width) : 웹 브라우저의 현재 화면 가로 크기의 1/100 이다. (화면 크기 변경에 따라 변화함.)  
vh(viewport height)


## text 제어 CSS 속성
font-size : .  
color : .  

font-family:[글꼴], [글꼴유형];  
글꼴유형을 generic-family 라고 부르며 (serif, sans-serif, cursive, fantasy, monospace 중 하나를 사용해야 한다.)
```css
h1{
    font-family: 'Times New Roman', Times, serif;
}
//앞에서부터 폰트 적용 우선순위이다.
//단, 글꼴유형은 고딕계열, 명조계열, 필기체계열 등 글꼴의 모양새를 나타내는 것이므로 항상 적용된다.
```

font-weight:굵기 단위;  
100~900, normal, bold, bolder, lighter 등을 사용한다.  
해당 글꼴에서 지원해야 제대로 적용이 된다.  

line-height:크기 단위 or 배수;  
글자의 줄높이(줄간격) 지정해준다.  
고정값으로 지정할 때는 해당 폰트사이즈보다 큰 값으로 지정해 주어야 글자가 겹치지 않는다.


## html 디버깅
css코드가 html에 적용이 안 되는 상황  
1. css 선택자 오류 없는가?
2. css 선택자 적용 우선순위 확인하기 (같은 선택자를 여러 번 적용했을 때, 가장 나중에 적용된 것이 큰 우선순위를 갖는다.)
3. css 속성값 오류 없는가?


## netlify 배포하기
무료 접속량 100gb  
netlify 주소 하나 줌.

react 프로젝트 배포 시, "script"의 build 명령 실행 후 생성된 build 폴더를 netlify에 올리면 된다.


## 이미지 링크와 이미지 맵
<이미지 링크>  
```html
<a href="#one">one으로 이동
    <img src="경로" alt="이미지 설명하는 대체 text">
</a>
이미지 누를 시 페이지 이동
```

<이미지 맵>  
하나의 이미지 안에서 여러 링크를 연결하고 싶을 때 사용한다.  
이미지를 좌표 속성으로 지정이 가능한 상태로 만들어서, 좌표값으로 링크 영역을 그려내는 것이다.

usemap 속성, `<map>` `<area>` 태그 사용 필요하다.   
```html
<img src="google.png" alt="구글이미지" usemap="#google" >
<map name="google">
    <area shape="" coords="" href="" alt="">
</map>

```

