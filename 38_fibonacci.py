# # Fibonacchi
# def fib(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         a, b = 0, 1
#         for _ in range(2, n + 1):
#             a, b = b, a + b
#         return b
# # Example usage
# n = 10
# print(f"The {n}th Fibonacci number is: {fib(n)}")


def fib (n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
            # whre a is the (n-2)th Fibonacci number and b is the (n-1)th Fibonacci number
        return a
# Example usage
n = 10  
print(f"The {n}th Fibonacci number is: {fib(n)}")