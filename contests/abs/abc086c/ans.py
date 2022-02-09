n = int(input())

def main():
  # t=0からスタート
  t_0 = 0
  # 初期位置の座標
  x_0 = 0
  y_0 = 0

  can = True
  for i in range(n):
    t, x, y = map(int, input().split())

    # 前回の位置から何歩進むか
    dt = abs(t - t_0)
    # 前回の位置からの絶対値
    dx = abs(x - x_0)
    dy = abs(y - y_0)

    # 次回の計算に使うため今回の値を保存しておく
    t_0 = t
    x_0 = x
    y_0 = y

    # dx+dyは最短距離、最短距離が歩数dtより大きかったら到達不可能
    if dt < (dx + dy):
      can = False  
    
    # 座標(x,y)に向かう最短距離dx+dyの偶奇と歩数dtの偶奇は一致する
    # 一致しなければ到達不可能
    if (dx + dy) % 2 != dt % 2:
      can = False

  if (can == True):
    print("Yes")
  else:
    print("No")

main()
