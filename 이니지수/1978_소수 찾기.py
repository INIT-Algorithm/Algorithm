n = int(input())
num = map(int, input().split())

sum = 0
for i in num:
    zeroNum = 0
    if i == 1:                
        zeroNum +=1
    else:
        for j in range(2, int(i)):
            if i % j == 0:
                zeroNum+=1
    if zeroNum == 0:
        sum+=1
print(sum)