## python class

```python
import math

#도형
class Shape :
    cal_count = 0
    figure = "Shape"

    @classmethod
    def class_printFigure(cls) :
        return cls.figure
    
    @staticmethod
    def static_printFigure() :
        return Shape.figure

#도형 상속 삼각형
class Triangle(Shape) : 
    figure = "triangle"
    
    def __init__(self, b, h=5) :
        self.b = b
        self.h = h
        
    def area(self) :
        Shape.cal_count += 1
        
        return self.b * self.h / 2

#도형 상속 정삼각형
class EquTriangle(Triangle) : 
    figure = "equilateral triangle"
    
    def __init__(self, b) :
        self.b = b
        
    def area(self) :
        Shape.cal_count += 1
        
        return 0.25 * math.sqrt(3) * self.b ** 2
    
    def circumference(self) :
        return self.b * 3

#도형 상속 원
class Circle(Shape) :
    figure = "circle"
    
    def __init__(self, r) :
        self.r = r
        
    def area(self) :
        Shape.cal_count += 1
        
        return math.pi * self.r ** 2
    
    def circumference(self) :
        return 2 * math.pi * self.r

tri = Triangle(10, 4)
eqtri = EquTriangle(3)
cir = Circle(8)

print(cir.static_printFigure(), cir.area(), cir.circumference())
print(tri.class_printFigure(), tri.area(), cir.circumference())
print(eqtri.class_printFigure(), eqtri.area(), cir.circumference())

print(Shape.cal_count, cir.cal_count, tri.cal_count)
```

인스턴스 메서드
클래스의 인스턴스 필드를 self. 를 통해 접근할 수 있다.

자식 클래스로 생성한 인스턴스는 부모 클래스의 메소드에 접근할 수 있지만, 부모 클래스로 생성한 메소드는 자식 클래스의 메소드에 접근할 수 없다.

자식 클래스에서 부모 클래스의 메소드를 재정의 하는 것을 '메소드 오버라이딩(method overriding)' 이라 한다.

@classmethod
클래스 매서드를 통해 자신의 클래스 변수에 접근 가능하다.
부모 클래스에서 선언된 클래스 메서드는 자식 클래스의 인스턴스의 클래스 변수를 참조할 수 있다.


@staticmethod
원본 클래스에서만 접근 가능.
인스턴스 변수에 접근할 수 없다.
정적 메서드는 객체 필드와 독립적이지만 로직상 클래스 내에 포함되는 메서드에 사용한다.


## 다형성
객체 지향 프로그래밍에서 클래스는 '다형성'을 가진다.
다형성 : 같은 속성을 가진 객체끼리 묶고, 같은 기능은 부모 클래스의 메소드를 사용하거나 필요에 따라 재정의 하는 것. 즉, 같은 정보를 공유하는 인스턴스는 다형성을 가진다고 볼 수 있다.

### python의 다중상속
python은 '다중상속'을 지원한다. 부모 클래스를 여러 개 상속 가능하다.
```python
class First :
    name = "first"
    def __init__(self) :
        print("First class")
    
    def printFirst(self) :
        print("first")
        
class Second :
    name = "second"
    def __init__(self) :
        print("First class")
    
    @classmethod
    def printName(cls) :
        print(cls.name)

#상속해야 할 부모클래스가 두 개인 경우 충돌 가능
#파이썬은 MRO에 따라 다중 상속을 진행
class Third(First, Second) :
    pass

third = Third()
third.printName()
third.printFirst()
```
일반적으로는 상속 받을 부모 클래스 안에 같은 이름의 메서드가 있으면 어떤 것을 먼저 실행해야할지 모르기 때문에, 두 부모 클래스의 생성자 메서드가 충돌 가능성이 존재하기 때문에 다중 상속을 지원하지 않는다.

python은 MRO(Method Resolution Order, 메소드 탐색 순서)에 따른다. 상속 명시된 클래스 중 왼쪽에서 오른쪽 순서로 메소드를 찾고, 처음 찾은 것을 실행한다.
마찬가지로 클래스 변수의 이름이 같을 때에도, 왼쪽부터 우선순위로 접근한다.

### python은 오버로딩을 지원하지 않는다.
java 등의 객체지향 언어에서는 한 클래스 안에서 같은 이름의 메소드를 여러 번 선언 가능한 오버로딩(overloading)을 지원한다.
오버로딩으로 매개변수의 자료형이나 개수가 다를 때 유형에 따라 여러 메소드를 선언가능하다.

python에서는 같은 이름의 메서드가 여러 번 선언되어 있으면 맨 마지막 메소드가 실행된다.

python은 자료형에 대해서 유연하기 때문에, 함수에서 가변인자 함수와 같은 방식과, 변수에 자료형을 명시하지 않는 것 때문에 오버로딩을 지원하지 않는다.