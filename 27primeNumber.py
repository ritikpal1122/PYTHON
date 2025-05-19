# prime number 
# A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")