n = int(input())
l = sorted(list(map(int, input().split())))
ans = 0

for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      # 3つの長さが全部違う かつ 一番長い辺よりその他2辺の合計の方が長い
      if (l[i] != l[j] and l[i] != l[k] and l[j] != l[k] and l[i] + l[j] > l[k]):
        ans += 1
print(ans)
