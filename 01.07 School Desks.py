x = int(input("Enter Classroom A: "))
y = int(input("Enter Classroom B: "))
z = int(input("Enter Classroom C: "))

a = x // 2
b = a + (x % 2)

aa = y // 2
bb = aa + (y % 2)

aaa = z // 2
bbb = aaa + (z % 2) 

print(b + bb + bbb)