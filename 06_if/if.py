#조건문
"""
if 조건:
    조건이 참일 때 실행할 코드
"""

# num = int(input("숫자를 입력하세요: "))
# if num > 0:
#     print("양수입니다.")
# else:
#     print("이 숫자는 0이거나 음수입니다.")

#if elif else문
# score = int(input("점수를 입력해주세요: "))
# if score >= 90:
#     print("A 학점입니다.")
# elif score >= 80:
#     print("B 학점입니다.")
# elif score >= 70:
#     print("C 학점입니다.")
# elif score >= 60:
#     print("D 학점입니다.")
# else:
#     print("F 학점입니다.") #가장 먼저 만나는 조건만 충족하면 끝. 한가지만 적용 if - elif - else 구조

#실습 1
#숫자를 입력받고 조건문으로 홀짝 판별
# n = int(input("홀짝 판별할 숫자를 입력하세요: "))
# if n > 0 and n % 2 == 0:
#     print("짝수입니다.")
# elif n > 0 and n % 2 == 1:
#     print("홀수입니다.")
# else:
#     print("자연수를 입력하십시오.")

#실습 2
#나이를 입력받고 학생 여부도 입력받기(y/n)
#20세 이상이면서 학생이면 성인 학생입니다.
#아니면 성인 학생이 아닙니다.

age = int(input("나이를 입력하세요.: "))
student = input("학생이신가요? (y/n): ")

if age >= 20 and student == "y":
    print("성인 학생입니다.")
else:
    print("성인 학생이 아닙니다.")