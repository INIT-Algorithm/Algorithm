#1431_시리얼 번호
# sort 함수 이용
# 시리얼번호 : 알파벳 대문자(A-Z) ,숫자(0-9) 로 이루어짐
# 1. 길이 짧은 것이 앞으로
# 2. 길이 같을 때, a의 모든 자리수의 합(숫자만)과 b의 모든 자리수의 합(숫자만) 중에 작은 합이 앞으로
# 3. 1,2번 조건으로도 비교 안되면, 사전 순으로 -> 숫자가 알파벳 보다 앞
# lamda식을 이용한 정렬 arr.sort(key = lambda x : (정렬기준1, 정렬기준2, 정렬기준3, …))

import sys
n = int(input())

def sum_num(num):
    result = 0 # result : 모든 자리수의 합
    for i in num:
        if i.isdigit(): # isdisit() : 문자열이 숫자인지 true/false
            result += int(i) 
    return result

arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip())

# 1. len(x) = 길이 
# 2. sum_num(x) = 모든 자리수의 합 
# 3. x = 사전순
arr.sort(key = lambda x:(len(x), sum_num(x), x))

for i in arr:
    print(i)