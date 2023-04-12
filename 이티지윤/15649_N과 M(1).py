#itertools의 permutations 함수를 사용해서 풀어보자.
#permutations(iterable, r) : iterable에서 원소 개수가 r개인
#순열을 뽑는 것

import itertools
#from itertools import permutations

n, m = map(int, input().split()) # 1부터 n까지 수 안에서 요소가 m개인 순열 만들기
#nums [ i for i in range(1, n+1)]

arr = []
for i in range(n+1):
    arr.append(i);
#[1,2,3,4]


pe = itertools.permutations(arr,m) #12게
#[(1,2), (1,3), (1, 4)]

for i in pe: #12개만큼 반복
    for j in i:
        print(j, end=' ') # 1 2
    print()

