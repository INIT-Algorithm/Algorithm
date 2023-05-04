n = int(input())
num = list(range(1, n))
m = int(input())

't번째 자리'

result=[]
def pick(t):
    for a in range(n-m+1):
        if t != 1 and result != []:
            if result[t-2] < num[t-1+a]:
                result.append(num[t-1+a])
                if t<m:
                    pick(t+1)
                elif t == m:
                    print (*result, "\n")
                    del result[m-1]
    if t >= 2:
        del result[t-2]

pick(1)
