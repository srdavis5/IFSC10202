km = int(input("Enter Length of Race in Kilometers: "))
min = int(input("Enter Minutes: "))
sec = int(input("Enter Seconds: "))
x = min / 60
y = sec / 3600
time = x + y
mile = km / 1.61
mph = mile / time
print(mph)