
#给出两个数，求出他们是哪两个数的最大公约数和最小公倍数，然后输出。
#小的在前，若有多组解，输出和最小的哪一组
def fun(a,b):
    "首先找出所有符合条件的数"
    l = {}
    result = []
    for i in range(1, b):
        for j in range(1, b):
            if (i % a == 0) and (j % a == 0) and (i * j / a == b):
                key = i
                value = j
                l[key] = value
    "将这些符合条件的数字之和存储在列表中"
    for key,value in l.items():
        result.append(key + value)
    "考虑到这两个数互质，或者其中一个数字为另外一个数字的约数的情况（列表为空）"
    if result: 
        b = min(result) 
        for key,value in l.items():
            if (key + value) == b and (key < value):
               print(key, value)
    else:
        print(a,b)
fun(1,6)

