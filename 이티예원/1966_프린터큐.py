import sys

#테스트 케이스 개수
total = int(input())
arr = []

for a in range(total):

    #문서의 개수 n, 궁금한 문서의 인덱스m
    n, m = map(int, input().split())

    #문서의 인덱스와 중요도를 묶은 리스트 
    arr = list(enumerate(list(map(int,input().split()))))
    
    #순서를 알고싶은 문서의 인덱스와 중요도를 묶은 리스트
    printer = arr[m]

    #count) 해당 문서가 인쇄된 순서를 저장
    count = 0

    while len(arr):

        #big) 배열의 가장 높은 우선순위
        big = max(i[1] for i in arr)
        
        #제일 앞에 있는 문서의 우선순위가 가장 높다면
        if arr[0][1] == big:
            #해당 문서를 pop()
            nowIdx = arr.pop(0)
            count += 1

            if nowIdx == printer:
                print(count)
                break

        #제일 앞에 있는 문서의 우선순위가 가장 높지 않다면
        else:
            #제일 앞에서 빼고
            nowIdx = arr.pop(0)
            #제일 마지막에 넣어준다
            arr.append(nowIdx)
