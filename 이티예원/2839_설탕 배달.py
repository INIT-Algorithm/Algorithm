N = int(input())
bag = 0

while N >= 0:
  
  # 봉지 수를 최소로 만들기 위해서
  # 5kg 봉지 수를 최대로
  # 3kg 봉지 수를 최소로 만들어야 함

  # 5의 배수인 경우
  if N % 5 == 0:
    bag += int(N // 5)
    print(bag)
    break
  
  # 5의 배수가 아닌 경우
  # 5의 배수로 만들기 위해서
  N -= 3    # 배달 해야 하는 설탕 -3kg
  bag += 1  # 가져가야하는 봉지 수 +1
  # 1. 5의 배수가 될 때까지 
  # 2. 또는 정확하게 N킬로그램으로 만들 수 없음이 확인될 때 까지 반복
  
else:
  print(-1)
