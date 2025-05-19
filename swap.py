a = 2 
b = 3
# a = a + b // with this we are usign a extra bit 
# b = a - b
# a = a - b

# temp = a
# a = b
# b = temp

# xor 
a = a ^ b
b = a ^ b
a = a ^ b

#stack 
a,b = b,a ## it goes into stack and then comes out 

print("a:", a)
print("b:", b)