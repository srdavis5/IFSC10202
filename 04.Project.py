height = int(input("Enter maximum height: "))
for y in range(1, 2 * height):
    x = height - abs(y - height)
    print("*" * x)