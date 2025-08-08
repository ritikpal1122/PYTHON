# factorial of a number 

# eg n=5 => # 5! = 5 * 4 * 3 * 2 * 1 = 120
def fact(n):
    if n == 0:
        return 1
    elif n < 0:
        return "Factorial is not defined for negative numbers"
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result
# Example usage
n = 5
print(f"The factorial of {n} is: {fact(n)}")  # Output: 120