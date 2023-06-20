import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0 for _ in range(M)]
# arr : 입력 받은 M개의 숫자가 차례로 담기는 리스트

# dfs(cnt) : 숫자를 cnt개 선택한 상태에서 arr[cnt]를 고르는 함수
def dfs(cnt):
    if cnt == M:    # 재귀함수 dfs(cnt) 종료 조건
        print(' '.join(map(str, arr)))
        return

    # cnt != m 인 경우,
    # 숫자를 더 선택해야 함
    for i in range(1, N + 1):   # 1 부터 n까지의 숫자를 이번 칸에 한번씩 넣어 줌
        arr[cnt] = i
        dfs(cnt+1)  # 다음 칸 숫자를 선택하는 다음 깊이 탐색 호츌

dfs(0)
