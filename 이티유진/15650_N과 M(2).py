from itertools import combinations    #itertools의 combinations 함수

n,m = map(int, input().split())   # N과 M 입력받기

a = []    # [1,2,3,4 ..]
for i in range(1,n+1):
		a.append(i)

for i in combinations(a,m):    # a에서 원소 개수 m개인 조합을 뽑는 것, 출력
		for j in i:
				print(j,end=' ')
		print()