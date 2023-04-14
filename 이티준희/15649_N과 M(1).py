#2023-04-06-Week1
#15649_N과 M(1)

#itertools의 permutations 함수를 사용해서 풀어보자
#permutations(iterable, r) : iterable에서 원소 개수가 r개인 순열을 뽑는 것

import itertools
import sys
#from itertools import permutations -> 함수 사용시 도트연산자 앞부분 생략 가능

n, m = map(int, input().split())

nums = [i for i in range(1, n+1)]

nums = []
for i in range(1, n+1) :
    nums.append(i)

arr = itertools.permutations(nums, m)


for i in arr : #리스트 원소 개수 -> set이 하나
    for j in i : 
        print(j, end=' ')
    print()