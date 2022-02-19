a, b = map(int, input().split())
ans = 0

for i in range(a, b+1):
  # 下1桁目
  s = i % 10
  # 上1桁目
  t = i // 10000 % 10

  # 下2桁目
  u = i // 10 % 10
  # 上2桁目
  v = i // 1000 % 10

  if (s == t and u == v):
    ans += 1
print(ans)
