#Person => name, age, email 속성 // name은 기본값으로 홍길동
#introduce 메소드 => 자기 자신을 소개하는 메소드

class Person:
    def __init__(self, age, email, name="홍길동"):
        self.age = age
        self.email = email
        self.name = name

    def introduce(self):
        print(f"제 이름은 {self.name}이고 나이는 {self.age}이고 이메일은 {self.email}입니다.")

person1 = Person(21, "jiwon7785@naver.com", "하지원")
person1.introduce()

person2 = Person(20, "gildong@gmail.com")
person2.introduce()

person2.address = "부산 진구" #person2 객체에 address라는 새로운 속성을 동적으로 추가
print(person2.address)

setattr(person1, "address", "부산 중구")
print(person1.address)

