### 소수의 개수 찾기
n = int(input()) # 입력받을 숫자 갯수

nums = list(map(int, input().split())) # 공백으로 숫자 구분
# 입력받은 n개의 숫자 ex: [1, 3, 5, 7]

prime_cnt=0 #소수 갯수
isPrime = True #소수 여부

for i in nums:
    if i == 1:
        continue
    for j in range(2, i): # nums에 있는 숫자 i를 2부터 i-1까지 나눔
        if i % j == 0: # 나누어떨어지면
            isPrime = False # 소수 아님
    if isPrime == True: # 소수이면
        prime_cnt += 1 # 소수 갯수+1 
print(prime_cnt)

