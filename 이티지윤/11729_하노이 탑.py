#11729_하노이 탑

n = int(input())

#n: 원판 수
#a,b,c : 3개의 장대
def top(n, a, b, c):# n개의 원판을 a에서 c로 옮기는 하노이 탑

    # 원판 1개 : a->c로 옮기면 끝
    if n == 1:
        print(a, c)
    
    # 재귀
    else:
        top(n-1, a, c, b) # a에 있는 원판 n-1 개를 b로 옮김
        print(a, c) # a에 남아 있던 가장 큰 n번 원반을 c로 옮김
        top(n-1, b, a, c) # b의 n-1 개의 원반을 c로 옮김
        
sum = 2 ** n - 1 # 이동 횟수 = 2^n-1
print(sum)

top(n, 1, 2, 3)