n = int(input())    # 수의 개수 N 입력 받기
numbers = map(int, input().split())    # N개의 수 입력 받기
count = 0    # 소수의 개수를 세기 위한 변수 count 초기화

for num in numbers:
    a = 0
    if num > 1 :    
        for i in range(2, num):  # 2부터 (num-1)까지 (자기자신 제외)
            if num % i == 0:
                a += 1  # 2와 (num-1) 사이 숫자로 나누어 떨어지면 a 1씩 증가
        if a == 0:
            count += 1  # a == 0 이면 소수이므로 count 1씩 증가
print(count)