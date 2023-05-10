
#2023-05-04-Week3-과제
#2579_계단 오르기


import sys
input = sys.stdin.readline

n = int(input())  #계단 개수
score = [0 for i in range(301)]  #계단 점수 리스트 -> 계단의 개수 300이하의 자연수
dynamic = [0 for i in range(301)]  #동적 계획법 리스트 -> 계단의 개수 300이하의 자연수

for i in range(n) : 
        score[i] = int(input()) #계단 개수만큼 점수 입력

'''
마지막 도착 계단은 반드시 밟아야 함
-> 계단 개수 입력 값이 a일 때
   마지막 도착 계단인 a번 계단을 x번째 차례에 밟은 계단이라고 하면
   x-1번째 차례에는 a-1번 계단이나 a-2번 계단을 밟았을 것
-> a-1번 계단을 밟았다면 a-2번째 계단은 밟을 수 없음

해당 인덱스번째 계단까지의 최댓값을 
동적 계획법 리스트에 저장

i번 계단까지 최댓값
= i-2번 계단까지 점수를 고려한 최댓값 + i번 계단의 점수 ,
  i-3번 계단까지 점수를 고려한 최댓값 + i-1번 계단의 점수
  중 더 큰 값 (max로 비교)
'''

dynamic[0] = score[0]
dynamic[1] = score[0] + score[1]
dynamic[2] = max (score[1]+score[2],  score[0]+score[2])

for i in range(3,n): 
    dynamic[i] = max(dynamic[i-3]+score[i-1]+score[i],  dynamic[i-2]+score[i])
print(dynamic[n-1]) 


###########################################################################################
#미리 리스트의 공간을 모두 할당 받는(?)건 낭비인가? 싶어서 다시 작성해봤지만 런타임에러 뜸

n = int(input())  #계단 개수
score = []   #계단 점수 리스트 -> 계단 개수만큼만 할당
for x in range(n) :
    score.append(int(input())) 
dynamic = []   #동적 계획법 빈 리스트 

if n == 1:
    dynamic.append(score[0])
    print(dynamic[0])
elif n == 2 :
    dynamic.append(max(score[0]+score[1],  score[1]))
    print(sum(score))
else : # n >= 3
    '''
    dynamic[0] = score[0]
    dynamic[1] = score[0] + soore[1]
    for i in range(2,n): 
        dynamic[i] = max(dynamic[i-3]+score[i-1]+score[i],  dynamic[i-2]+score[i])
    print(score[-1])

    '''
    dynamic.append(max(dynamic[i-2]+score[i] ,   dynamic[i-3]+score[i]+score[i - 1]))

print(dynamic[-1]) #마지막으로 저장한 값 출력 ->  d[n-1] == d[-1] == d.pop()


