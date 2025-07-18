# print(10/0)

# try:
#     print(10/0)
# except:
#     print("예외 발생!!")
#
# try:
#     num = int(input("숫자를 입력해주세요: "))
#     print(10/num)
# except ValueError: #값 데이터 오류
#     print("문자말고 숫자 넣으세요.")
# except ZeroDivisionError:
#     print("0말고 다른 숫자 넣으세요.")

#IndexError, ValueError
# try:
#     my_list = [1, 2, 3]
#     index = int(input("리스트에서 가져올 인덱스: "))
#     print(my_list[index])
# except ValueError:
#     print("숫자만 입력해라")
# except IndexError:
#     print("그런 인덱스는 없다.")

#파일 입출력 예외 처리: FileNotFoundError
# file = None
# try:
#     file = open("hi.txt", "r", encoding="utf-8")
#     content = file.read() #파일의 내용을 읽어온다.
#     print(content)
# except FileNotFoundError:
#     print("그런 파일은 없다.")
# finally:
#     if file is not None and not file.closed:
#         file.close()
#         print("정상적으로 파일이 닫혔습니다.")
#     elif file is None:
#         print("애초에 열리지 않았음")

# try:
#     print("hello")
#     print(a) #오류나는 순간에 except로 넘어감!
# except:
#     print("bye")

#리스트 요소 5개 선언하고 index로 찾는 로직
#IndexError, ValueError 예외 처리
#정상적이면 해당 리스트 값 출력
#마지막은 항상 끝!! 출력

list1 = ["가", "나", "다", "라", "마"]

# try:
#     index = int(input("찾으려하는 인덱스 값을 입력하시오: "))
#     result = list1[index]
# except IndexError as message:
#     print("해당 인덱스는 존재하지 않습니다.")
#     print(message)
# except ValueError as message:
#     print("찾으려는 인덱스 값을 정수로 입력하십시오.")
#     print(message)
# else:
#     print(result)
# finally:
#     print("끝!!")
#
# try:
#     index = int(input("찾으려하는 인덱스 값을 입력하시오: "))
#     print(list1[index])
# except IndexError:
#     print("해당 인덱스는 존재하지 않습니다.")
# except ValueError:
#     print("찾으려는 인덱스 값을 정수로 입력하십시오.")
# finally:
#     print("끝!!")

#raise 키워드: 강제로 예외를 발생시키기
#특정 조건에서 개발자가 직접 예외를 발생시키는데 사용
# try:
#     age = int(input("나이를 입력하시오: "))
#
#     if age < 0 or age > 150:
#         raise Exception("0 이상 150 미만의 숫자만 입력해주세요.")
# except Exception as e:
#     print(e)
# else:
#     print(f"입력된 나이: {age}")
# finally:
#     print("끝!!")

#사용자 정의 예외 클래스
# class AgeException(Exception):
#     def __init__(self):
#         super().__init__("0 이상 150 미만의 숫자만 입력하십시오.")
#
# try:
#     age = int(input("나이를 입력하세요: "))
#     if age < 0 or age > 150:
#         raise AgeException()
# except AgeException as e:
#     print(e)
# else:
#     print(f"입력된 나이: {age}")
# finally:
#     print("끝!!")

#출금을 할 때 잔액이 부족하면 발생되는 예외
#FundsError => 잔액이 부족합니다. 현재 잔액 ***원, 출금 시도 금액 ***원
#Account 클래스 만들고 출금 매소드 withdraw
#출금할 때 잔액이 부족하면 FundsError를 발생

#내꺼
# class FundsError(Exception):
#     def __init__(self):
#         super().__init__("잔액이 부족합니다.")
#
# class Account:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance
#         print(f"{self.name}님의 계좌가 개설되었습니다. 현재 잔액: {self.balance}원")
#
#     def withdraw(self, minus):
#         try:
#             new_balance = self.balance - minus
#             if self.balance < 0:
#                 raise FundsError
#         except FundsError as e:
#             print(e)
#             print(f"현재 잔액 {self.balance}원, 출금 시도 금액 {minus}원")
#         else:
#             print(f"{minus}원 출금되었습니다. 현재 잔액: {self.balance}원")
#
# account1 = Account("하지원", 100)
# account1.withdraw(200)


#강사님꺼
class FundsError(Exception):
    def __init__(self, balance, minus): #생성자에서 현재 잔액과 출금 시도 금액을 받습니다.
        super().__init__(f"잔액이 부족합니다. 현재 잔액 {balance}원, 출금 시도 금액 {minus}원")

class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, minus):
        try:
            if minus > self.balance:
                raise FundsError(self.balance, minus)
        except FundsError as e:
            print(e)
        else:
            self.balance -= minus
            print(f"정상적으로 출금되었습니다. 남은 잔액: {self.balance}")

account1 = Account(10000)
account1.withdraw(20000)
account1.withdraw(5000)

#딕셔너리 요소 찾기
#딕셔너리 키를 입력받는다(숫자로)
#result 변수에 해당 키의 값을 넣음
#예외처리 => 해당 키가 존재하지 않을 때 "KeyError" 처리: "해당 키는 존재하지 않습니다." 출력
#숫자가 아닌 문자를 입력했을 때 "ValueError" 처리: "숫자를 입력해주세요." 출력
#정상적으로 실행된다면 해당 키의 값을 넣어둔 result 출력
#마지막은 항상 "완료!!"를 출력

dict1 = {1 : "가", 2 : "나", 3: "다"}

try:
    a = int(input("딕셔너리에서 찾을 키(숫자)를 입력하시오: ")) #ValueError가 발생할 수 있는 코드
    result = dict1[a] #KeyError가 발생할 수 있는 코드
except KeyError:
    print("해당 키는 존재하지 않습니다.")
except ValueError:
    print("숫자를 입력해주세요.")
else:
    print(result)
finally:
    print("완료!!")