a = [1,5,80]
result = 1
for item in a:
    result = result * item

b = str(result)
num = 0 
for item in b:
    if item == "0":
        num += 1
print("The result is %4d." % num)


    
    
