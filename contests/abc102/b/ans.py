n = int(input())
a = list(map(int, input().split()))
ans = 0

for i in range(n):
  for j in range(n):
    diff = abs(a[i] - a[j])
    ans = max(ans, diff)

print(ans)
