# Break Continue Pass   
# 1. Break: used to exit a loop or switch statement.
# 2. Continue: used to skip the current iteration of a loop and move to the next iteration.
# 3. Pass: used as a placeholder in loops, functions, or classes where no action is required.

x = int(input("How Many Candies You Want?"))

i = 1
# while i <= x:
#     print("You have reached the limit of 5 candies.")
#     i += 1

while i <= x:
    if i > 5:
        print("You have reached the limit of 5 candies.")
        break
    print("You have", i, "candies.")
    i += 1
    
print("Loop ended.")


# continue
# The continue statement is used to skip the current iteration of a loop and move to the next iteration.
#it only skips the current iteration


#pass
# The pass statement is a null operation; it does nothing when executed.