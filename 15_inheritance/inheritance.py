#부모 클래스(Super Class)
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} 동물 객체 생성!")

    def speak(self):
        print("동물이 소리를 냅니다.")

    def move(self):
        print(f"{self.name}이(가) 움직입니다.")

#----- 상속 시작 -----

#자식 클래스(Sub Class)
#괄호 안에 부모 클래스 이름을 명시해서 상속 선언
class Dog(Animal):
    def wag(self):
        print(f"{self.name}이(가) 꼬리를 흔듭니다.")

    def speak(self): #부모 클래스의 speak 메소드를 재정의(Overriding)
        print("왈왈")

class Cat(Animal):
    def speak(self):
        print("애옹")

    def clim(self):
        print(f"{self.name}이(가) 높은 곳에 올라갑니다.")

animal1 = Animal("일반 동물")
animal1.speak()
animal1.move()

dog1 = Dog("방울이")
dog1.speak()
dog1.move()
dog1.wag()

cat1 = Cat("냐옹이")
cat1.speak()
cat1.move()
cat1.clim()

#실습
#Shape라는 부모 클래스 => 속성 color
#메소드 describe => 이 도형의 색깔은 ***입니다. 출력

#Circle 자식 클래스
#메소드 describe 오버라이딩 => 이 원의 색깔은 ***입니다. 출력
#메소드 get_area(radius) => math.pi 모듈을 이용해서 넓이 구해서 리턴(소수점 둘 째자리 까지만)
#리턴한 것을 출력할 때 소수점 둘 째 자리까지

import math
class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self):
        print(f"이 도형의 색깔은 {self.color}입니다.")

class Circle(Shape):
    def describe(self): #오버라이딩
        print(f"이 원의 색깔은 {self.color}입니다.")

    def get_area(self, radius):
        return math.pi * (radius ** 2)

circle1 = Circle("빨간색")
circle1.describe()
print(f"원의 넓이: {circle1.get_area(5):.2f}")