#Account 클래스 => 계좌 정보
#owner 그리고 balance => 잔액은 생성될 때 0으로 초기화
#deposit 메소드를 추가하여 잔액을 증가시키고 증가된 잔액을 출력(양수로만 입력받아야함)
#withdraw 메소드를 추가하여 잔액을 감소시키고 감소된 잔액을 출력(양수로 감소시켜야하고 잔액보다는 작아야함)
#만약에 잔액이 부족하다면 출금을 할 수 없도록 출력

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print(f"{self.owner}님의 계좌가 개설되었습니다. 잔액: {self.balance}")

    def deposit(self, plus):
        if plus > 0:
            self.balance += plus
            print(f"{plus}원 입금되었습니다. {self.owner}님의 현재 잔액은 {self.balance}원입니다.")
        else:
            print("입금할 금액을 양수로 다시 입력하십시오.")

    def withdraw(self, minus):
        if 0 < minus <= self.balance: #출금액이 0보다 작거나 잔액보다 많은 경우 방지
            self.balance -= minus
            print(f"{self.owner}님의 현재 잔액은 {self.balance}원입니다.")
        else:
            print("해당 금액만큼 출금할 수 없습니다.\n출금할 잔액을 양수이고 잔액보다는 작은 값으로 다시 입력하십시오.")

account1 = Account("하지원", 10000)
account1.deposit(20000)
account1.deposit(-1000)
account1.withdraw(13000)
account1.withdraw(20000)
account1.withdraw(-1000)