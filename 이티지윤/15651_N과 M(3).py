import sys
input = sys.stdin.readline

# dfs : 숫자를 cnt개 선택 후 arr[cnt]고르는 재귀함수
def dfs(cnt):
    if cnt == m: # m개를 모두 선택한 상태라면 더이상 숫자 선택X return시킴
        print(' '.join(map(str, arr))) 
        return
    for i in range(1, n + 1):
        arr[cnt] = i
        dfs(cnt + 1)

n, m = map(int, input().split())
arr = [0 for _ in range(m)] # arr : 고른 m개의 숫자가 차례로 담기는 리스트
dfs(0) # 아직 선택한 숫자 없음 cnt=0