#2023-05-18-Week6-과제
#15723_n단 논법

'''
n개의 전제가 있을 때 m개의 결론을 도출

입력 :
정수 n(2 ≤ n ≤ 26)
둘째 줄부터 n개의 줄에 걸쳐 각 줄에 전제가 하나씩
a is b의 형식
a는 b이면서 c일 수 없으나, a와 b가 동시에 c일 수는 있다.

출력 :
m개의 줄에 걸쳐 각 줄에 결론이 참인지 거짓인지
'''


#런타임 에러 발생

import sys
input = sys.stdin.readline

N = int(input())
graph = [[0] * 26  for i in range(26)]  


#입력한 알파벳 순서를 어떻게 정해야할까.............
order = "abcdefghijklmnopqrstuvwxyz" #알파벳 문자열의 인덱스로..?


for i in range(N) : 
    a, b = map(order.index, input().strip().split(" is "))
    graph[a][b] = 1

for i in range(26) :
    for j in range(26) :
        for k in range(26) :
            if graph[j][k] < graph[j][i] + graph[i][k] :
                graph[j][k] = graph[j][k]
            else :
                graph[j][k] = graph[j][i] + graph[i][k]

M = int(input())

for i in range(M) :
    a, b = map(order.index, input().strip().split(" is "))
    if graph[a][b] != 0 :
        print('T')
    else :
        print('F')