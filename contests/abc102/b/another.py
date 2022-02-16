n = int(input())
a = list(map(int, input().split()))
c_max = 1
c_min = 10**9

# 数列の最大値と最小値を探す
for i in range(n):
  c_max = max(a[i], c_max)
  c_min = min(a[i], c_min)

print(c_max-c_min)
