n = int(input())
h = list(map(int, input().split()))

# 制約条件の足場数より多い要素数の配列
dp = [float("inf")] * 100010

# 初期位置はコストが掛からないので0
dp[0] = 0

for i in range(1, n):
  dp1 = dp[i-1] + abs(h[i] - h[i-1])
  if dp[i] > dp1:
    dp[i] = dp1

  if (i > 1):
    dp2 = dp[i-2] + abs(h[i] - h[i-2])
    if dp[i] > dp2:
      dp[i] = dp2

print(dp[n-1]) 


