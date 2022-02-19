n, k = map(int, input().split())
l_list = list(map(int, input().split()))

l_list.sort()
l = len(l_list)
ans = 0
for e in l_list[l-k:l]:
  ans += e
print(ans)
