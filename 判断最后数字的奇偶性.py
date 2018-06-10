a = [1, 3, 3]
result = 1
for item in a:
    result = result * item
b = str(result)

if int(b[-1]) % 2 == 0:
    print("0")
else:
    print("1")
