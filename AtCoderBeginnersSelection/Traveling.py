N = int(input())

t_0 = 0
x_0 = 0
y_0 = 0

# プランが実行可能か判断するフラグ
flag = True

for n in range(N):
  t, x, y = map(int, input().split())
  dt = abs(t - t_0)
  dx = abs(x - x_0)
  dy = abs(y - y_0)

 # 前の値を保持
  t_0 = t
  x_0 = x
  y_0 = y

# tは時間だが、とどまることはできないので歩数と言い換えられる
# x+yは最短距離、最短距離が歩数より大きかったら到達不可能
  if dt < (dx + dy):
    flag = False
# 座標(x,y)においてx+yが偶数の時、たどり着くまでの歩数は必ず偶数回になる性質がある
  elif (dt % 2 != (dx + dy) % 2): # 歩数とx+yの偶奇の一致を確認
    flag = False

if flag == True:
  print("Yes")
else:
  print("No")
