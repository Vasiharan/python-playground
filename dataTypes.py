# Integer
result = 0
for i in range(10):
    result += i
print(result)

# List
L = list(range(10))
print(L)

typeL = type(L[0])
print(typeL)

# List of strings
L2 = [str(c) for c in L]
print(L2)

L3 = [True, "2", 3.0, 4]
L4 = [type(item) for item in L3]
print(L4)









