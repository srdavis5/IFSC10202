num1 = int(input("Enter First Number: "))
operator = input("Enter Operator (+,-,*,/): ")
num2 = int(input("Enter Second Number: "))

result = None

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print("Invalid")

if result is not None:
    print(f"{num1} {operator} {num2} = {result}")