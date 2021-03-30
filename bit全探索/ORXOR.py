from itertools import product
N = int(input())
A = list(map(int, input().split()))
ans = float('INF') # 答えをinfで初期化

# 仕切りがあるかないかをTrue or False, (N-1)の長さのtupleを全探索
for _bit in itertools.product((True, False), repeat=N - 1):
  bit = list(_bit) + [True]
  xored = 0
  ored = 0
  for i in range(N):
    ored |= A[i]
    # 区切りがある時は現在までのorしたものをxorして、oredを初期化
    if bit[i]:
      xored ^= ored
      ored = 0
  # 答えを最小値で初期化
  ans = min(ans, xored)
print(ans)
