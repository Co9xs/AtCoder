import math
from functools import lru_cache


MOD = 998244353

@lru_cache
def f(x):
  # 再帰は抜けるパターンを最初に書く
  if x <= 4:
    return x
  X1 = x//2
  X2 = (x+1)//2
  return f(X1) * f(X2) % MOD
  
X = int(input())
print(f(X))
