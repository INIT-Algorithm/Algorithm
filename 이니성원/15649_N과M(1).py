import sys
import itertools
n,m=map(int,sys.stdin.readline().split())    #map(적용시킬 함수, 적용할 값들) : 입력받은 값을 정수타입으로 변환
nums=[i for i in range(1,n+1)]    #i = 1 ~ n

arr=itertools.permutations(nums, m) #permutations(iterable, r) : iterable에서 원소개수가 r개인 순열 뽑기
# print(list(arr))

for i in arr:
    for j in i:
        print(j,end=" ")
    print()

