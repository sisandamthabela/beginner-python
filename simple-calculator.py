#Gather input from user
print('----------')
print('Calculator')
print('----------')
num1 = input('Choose a number: ')
num2 = input('Choose another number: ')

operator = input('Choose a operator (+, -, /, or *: )')

if operator == '+':
    ans = (int(num1) + int(num2))
    print(f" {int(num1)} ➕ {int(num2)} = {ans} ")
elif operator == '-':
    ans = (int(num1) - int(num2))
    print(f" {int(num1)} ➖ {int(num2)} = {ans} ")
elif operator == '/':
    ans = (int(num1) / int(num2))
    print(f" {int(num1)} ➗ {int(num2)} = {ans} ")
elif operator == '*':
    ans = (int(num1) * int(num2))
    print(f" {int(num1)} ✖️ {int(num2)} = {ans} ")
else:
    print('Invalid input, please try again later.')
