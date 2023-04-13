#2023-04-08-Week1-과제
#1978_소수 찾기

'''
입력 1 - 수의 개수 N < 100
입력 2 - 1000 이하의 자연수 N개 
결과 - 입력2의 자연수 중 소수의 개수 출력
'''

n = int(input())
#feedback ) n = int(input("입력 : \n")) -> input 내부에 추가적인 멘트 작성 x

num = list(map (int, input().split()))  # 입력 받는 값 여러 개 -> map 함수 : 자료형, 함수 (.split() 공백으로 구분)

result = 0 # 입력한 자연수 중 소수의 개수 

for i in num : # 입력 받은 수들을 소수 확인 대상 i로 설정
    cnt = 0 # 소수 확인 대상의 약수 개수
    if i == 1 : # 1은 소수 아님
        continue 

    for j in range (2, i+1) : # 2~i까지 
        if (i%j == 0) : # 소수 확인 대상이 2부터 자기 자신으로 나눴을 때 0 이 되면
            cnt += 1 # 약수 개수 증가

    if cnt == 1 : # 약수의 개수 1개
        result += 1  # 소수 개수 추가

print (result) # 출력 : 입력 자연수 중 소수의 개수

#feedback ) print ("출력 : ", result) -> 출력시 추가적인 멘트 x




    
        
           
    
    
