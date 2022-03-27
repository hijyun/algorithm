import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

dp = [[0] * 21 for _ in range(n)]

# 첫 번째 수는 무조건 저장해야하니까
dp[0][arr[0]] = 1

for i in range(1, n - 1):
    for j in range(21):
        if dp[i - 1][j]:
            if j + arr[i] <= 20:
                # 더하기 저장
                dp[i][j + arr[i]] += dp[i - 1][j]
            if j - arr[i] >= 0:
                # 빼기 저장
                dp[i][j - arr[i]] += dp[i - 1][j]

print(dp[n-2][arr[-1]])
