import sys
input = sys.stdin.readline

n = int(input())
score = []
dp = []

for _ in range(n):
    score.append(int(input()))

dp[0] = score[0]
dp[1] = score[0] + score[1]
dp[2] = max(score[0] + score[2], score[1] + score[2])
for i in range(3, n):
    dp[i] = max(score[i] + dp[i-2], score[i] + score[i-1] + dp[i-3])

print(dp[n-1])
