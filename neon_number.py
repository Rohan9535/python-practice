n = int(input("Enter a number: "))

square = n * n
sum = 0

while square > 0:
    digit = square % 10
    sum += digit
    square //= 10

if sum == n:
    print("Neon Number")
else:
    print("Not a Neon Number")