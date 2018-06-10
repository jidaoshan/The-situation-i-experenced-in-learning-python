#给出两个数，求出他们是哪两个数的最大公约数和最小公倍数，然后输出。
#小的在前，若有多组解，输出和最小的哪一组
def fun(a,b):
    l = {}
    result = []
    for i in range(1, b):
        for j in range(1, b):
            if (i % a == 0) and (j % a == 0) and (i * j / a == b):
                key = i
                value = j
                l[key] = value
    for key,value in l.items():
        result.append(key + value)
   
    if result: 
        b = min(result) 
        for key,value in l.items():
            if (key + value) == b and (key < value):
               print(key, value)
    else:
        print(a,b)
fun(1,6)
