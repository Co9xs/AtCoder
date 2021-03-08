N = int(input())
ans = -1
for i in range(N):
  A, P, X = map(int, input().split())
  if X - A > 0: # 家を出てから1分経つと、在庫が1台減っているので、A分ではA台減っている
    if ans == -1:
      ans = P
    else:
      ans = min(ans, P)
print(ans)
