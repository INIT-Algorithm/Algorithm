
N, M = map(int, input().split())

result = []

def sequence(numbers, M, result):
    if len(result) == M:
        print(' '.join(map(str, result))) # result 리스트 요소들을 공백을 기준으로 구분하여 문자열로 변환하고 한 줄에 출력
        return
    
    for i in numbers:
        result.append(i)
        sequence(numbers, M, result)
        result.pop()

numbers = list(range(1, N+1))
sequence(numbers, M, result)
