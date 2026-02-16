number = int(input("Enter a number: "))

tens = number // 10
ones = number % 10

swap = (ones * 10) + tens

print(f"Swapped number: {swap}")

