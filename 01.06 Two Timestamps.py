print("First Timestamp")
H = int(input("Enter Hours: "))
M = int(input("Enter Minutes: "))
S = int(input("Enter Seconds: "))

print("Second Timestamp")
h = int(input("Enter Hours: "))
m = int(input("Enter Minutes: "))
s = int(input("Enter Seconds: "))

H *= 3600
M *= 60
h *= 3600
m *= 60

total1 = H + M + S
total2 = h + m + s
print(total2 - total1)