# Nはお札の数、Yは合計金額
N, Y = map(int, input().split())

#　まずはx, yが決まると,zは一意に決まるので2重for文でOK（3重だと時間OVER）
for x in range(N+1):
  for y in range(N-x+1):
    if 10000*x + 5000*y + 1000*(N-x-y) == Y:
      print(x, y, N-x-y)
      exit()
print(-1,-1,-1)
