#15651_N과 M(3)
# -> 런타임에러 발생
N, M = map((int, input()).split())

list = []

def func() :
    if len(list) < M :
        for i in range(1, N+1) :
            list.append(i)
            func()
            list.pop() 
    
    else :
        print(*list)

func()