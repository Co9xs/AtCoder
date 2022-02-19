n, l = map(int, input().split())
s_list = [input() for _ in range(n)]
s_list.sort()

ans = ""
for s in s_list:
  ans += s

print(ans)
