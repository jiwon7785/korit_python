#산술 연산자
num1 = 30
num2 = 12

print(f"num1 + num2 = {num1 + num2}") #덧셈
print(f"num1 - num2 = {num1 - num2}") #뺄셈
print(f"num1 * num2 = {num1 * num2}") #곱셈
print(f"num1 / num2 = {num1 / num2}") #나눗셈(실수 몫 반환)
print(f"num1 // num2 = {num1 // num2}") #나눗셈(정수 몫 반환)
print(f"num1 % num2 = {num1 % num2}") #나머지

#대입 연산자
x = 10
x += 5 # x = x + 5 => 15
x *= 2 # x = x * 2 => 30
# x /= 5 # x = x / 5 => 6.0 (실수 몫)
x //= 5 # x = x // 5 => 6 (정수 몫)
print(x)

#비교 연산자
x = 10
y = 20
z = 10
print(x == z) #True
print(x > y) #False
print(x == y) #False
print(x != z) #False
print(x <= y) #True
print(x >= z) #True

#논리 연산자
a = True
b = False
print(a and not b) #True
print(a or b) #True
print(not b) #True