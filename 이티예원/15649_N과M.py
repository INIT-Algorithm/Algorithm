from itertools import permutations
import sys

print("1부터 N까지 자연수 중에서 중복 없이 M개 선택")

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

p_array = permutations(nums, m)
for i in p_array:
    for j in i:
        print(j, end = " ")
    print()
