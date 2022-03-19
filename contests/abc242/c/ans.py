n = int(input())
MOD = 998244353

# dp[i][j] := i桁で先頭がjである平坦数の個数
# (最大n桁で1-9の9通り)
dp = [[0] * 10 for _ in range(n+1)]

for j in range(1, 10):
  dp[1][j] = 1

for i in range(2, n+1):
  for j in range(1, 10):
    if j == 1:
      dp[i][j] = (dp[i-1][j] + dp[i-1][j+1])%MOD
    elif j == 9:
      dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%MOD
    else:
      dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1])%MOD

ans = 0
for j in range(1, 10):
  ans += dp[n][j]
  ans %= MOD

print(ans)
