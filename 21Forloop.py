#for loop
# A for loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.
# The syntax for a for loop is:

# x=[1,2,3,4,5]
x="Ritik"
for i in x:
    print(i)

for i in range(1, 50):
    if i % 2 == 0:
        print(i, end=" ")
    else:
        print(i) 
        

nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using a for loop to iterate over the list and print each number

for i in nums2 :
    print(i, end=" ")
    print("\n")
# how it does i+1 ? 
# Using a for loop to iterate over the list and print each number with increment
for i in nums2:
    print(i + 1, end=" ")
    print("\n")