#给你个小写英文字符串a和一个非负数b(0<=b<26), 将a中的每个小写字符替换成字母表中比它大b的字母。这里将字母表的z和a相连，如果超过了z就回到了a。

#例如a="cagy", b=3, 则输出 ：fdjb

def fun(a,b):
    cn = ['a', 'b', 'c', 'd','e', 'f','g','h', 'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    result = []
    a.split()
    for j in range(len(a)):
        for i in range(len(cn)):
            if cn [i] == a [j]:
                if (i + b ) < 25:
                    result.append(cn[i + b])
                else:
                    result.append(cn[i + b -26])
    return result
                
a = 'cagy'
b = 3
print(fun(a,b))


        
        
            
        