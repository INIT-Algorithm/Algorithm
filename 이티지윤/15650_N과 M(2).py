import itertools
n, m = map(int, input().split()) 

nums = [ i for i in range(1, n+1)] #1~n까지 nums에 넣기

arr = itertools.combinations(nums, m) #중복 제외, 순서 상관없는 조합 만들기
for i in arr:
    for j in i:
        print(j, end=' ') 
    print()