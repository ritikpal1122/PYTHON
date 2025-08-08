# Recursion Calling same function again and again

# i=0
# def check_recursion():
#     global i
#     i = i + 1
#     print(f"Recursion called {i} times")
#     check_recursion()

# check_recursion()



# limit Recursin 

import sys
sys.setrecursionlimit(2220)
def check_recursion():
    print("Recursion called")
    check_recursion()

try:
    check_recursion()
except RecursionError as e:
    print("Recursion limit reached:", e)
# Output:
# Recursion limit reached: maximum recursion depth exceeded in comparison