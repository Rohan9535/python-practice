n = int(input("Enter a number: "))

temp = n
sum = 0
product = 1

while temp > 0:
    digit = temp % 10
    sum += digit
    product *= digit
    temp //= 10

if sum == product:
    print("Spy Number")
else:
    print("Not a Spy Number")