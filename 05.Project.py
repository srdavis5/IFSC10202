x = int(input("Enter Start of Range: "))
y = int(input("Enter End of Range: "))

print(f"Special Numbers between {x} and {y}")

for num in range(x, y + 1):
    order = len(str(num))
    value = 0
    temp = num
    
    while temp > 0:
        digit = temp % 10
        value += digit ** order
        temp //= 10
    if num == value:
        print(num)