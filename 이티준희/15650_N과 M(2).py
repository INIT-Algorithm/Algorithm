#2023-04-08-Week1-과제
#15650_N과 M(2)

'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

입력 : 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
출력 : 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

'''


'''
#feedback ) combinations 만 사용해도 풀이 가능
from itertools 
n,m = map(int,input().split())
num = itertools.combinations([i for i in range(1,n+1)],m)

for i in num :
    j = itertools.permutations(i) #permutation 가능한 모든 순열 
    for k in j :
        if k == sorted(k) : #오름차순으로 정렬된 경우면 출력
            print("  ".join(map(str, k))) 
            #map k의 요소들을 문자열로 반환
            #join 리스트 요소를 문자열로 연결
            #"  "로 요소 사이에 구분자
'''
from itertools import combinations  
 
n,m = map(int,input().split())

arr = []  
for i in range(1,n+1):
		arr.append(i)

for i in combinations(arr,m):  
		for j in i:
				print(j, end=' ')
		print()

