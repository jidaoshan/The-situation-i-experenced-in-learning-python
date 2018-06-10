a = 7
b = bin(a)
num = 0
for item in b:
    if item == '1':
        num += 1
print("The result is %4d." % num)
